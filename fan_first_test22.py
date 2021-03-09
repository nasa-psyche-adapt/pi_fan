# WE KNOW THIS WORKS TO CONTROL THE FAN. NEED TO UPDATE IT TO BE A ROS NODE


import board
from time import sleep
import RPi.GPIO as GPIO        # need this?

print("hello")
	
#if userinput 1 fan on 2 fan off
#else fan on

fan = 26

GPIO.setmode(GPIO.BCM) 			# initializes that 26 is the GPIO26 pin
GPIO.setup(fan, GPIO.OUT)
	
	
def fanControl():

	while True:
		GPIO.output(fan, GPIO.HIGH)
		print("Fan on")
	
	
	
if __name__ == '__main__':
	try:
		fanControl()
	except KeyboardInterrupt:
		GPIO.output(fan,GPIO.LOW)
		GPIO.cleanup()
		sleep(1)
		pass
