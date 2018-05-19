
from Adafruit_AMG88xx import Adafruit_AMG88xx
import os
import math
import time
import csv

import numpy as np


from colour import Color

#low range of the sensor (this will be blue on the screen)

#high range of the sensor (this will be red on the screen)

#how many color values we can have

os.putenv('SDL_FBDEV', '/dev/fb1')

#initialize the sensor
sensor = Adafruit_AMG88xx()

points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
grid_x, grid_y = np.mgrid[0:7:32j, 0:7:32j]

time.sleep(.1)

mode = 1	

while(1):
	
	if mode = 0
	#read the pixels
	oscmsg = OSC.OSCMessage()
	oscmsg.setAddress("/thermal_zero")
	oscmsg.append(sensor.readPixels())
	
	
	else 
		
