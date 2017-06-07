import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
count = 0

def handler(channel):
	global count
	if count > 2 :
		count = 0
	count = count + 1 
	print count

GPIO.add_event_detect(24, GPIO.RISING, callback=handler, bouncetime=300)

while True:
	if count == 1:
 		print "play"
		count = 0

	elif count ==2 :
		print "delete"
		count = 0

	time.sleep(1)
