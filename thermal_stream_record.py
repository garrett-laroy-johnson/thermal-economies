
from Adafruit_AMG88xx import Adafruit_AMG88xx
import os
import math
import time
import csv
from OSC import OSCClient, OSCMessage


import numpy as np

from datetime import datetime


os.putenv('SDL_FBDEV', '/dev/fb1')

#initialize the sensor
sensor = Adafruit_AMG88xx()
points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
grid_x, grid_y = np.mgrid[0:7:32j, 0:7:32j]

time.sleep(1)

#initialize OSC client
client = OSCClient()
client.connect(('224.0.0.1', 9876))

#initialize CSV file
now = datetime.now()
filename = 'recordings/'+'%02d-%02d-%04d_%02d-%02d-%02d.csv' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
write_header = not os.path.exists(filename) or os.stat(filename).st_size == 0


	#replace with thermal data
	#row = sensor.readPixels()
	
with open(filename, "a") as f_output:
	csv_output = csv.writer(f_output)

	if write_header:
		csv_output.writerow(["hour","second","minute","sensor_data"])
	
	
	while(1):


		client.send( OSCMessage("/thermal_zero", sensor.readPixels()))
		now = datetime.now()
		row = [(now.hour), (now.minute), (now.second),(sensor.readPixels())]
		csv_output.writerow(row)
		#time.sleep(.1)
    		#f_output.flush()
		