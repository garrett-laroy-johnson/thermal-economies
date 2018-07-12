from Adafruit_AMG88xx import Adafruit_AMG88xx
from time import sleep 
from os import putenv 
from OSC import OSCClient, OSCMessage 
from socket import gethostname
import time


putenv('SDL_FBDEV', '/dev/fb1')

#get socket/hostname
id = gethostname()

#initialize the sensor
sensor = Adafruit_AMG88xx()
sleep(.1)

#initialize OSC client
client = OSCClient()
client.connect(('192.168.200.246', 9876))
#224.0.0.1

#run code, read sensor	
while(True):
	client.send( OSCMessage("/thermal/"+id, sensor.readPixels()))


