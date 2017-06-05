import RPi.GPIO as GPIO
import time
import pygame
import sys
pygame.init()

sound = pygame.mixer.Sound("output1.wav")

channel = sound.play()

pin = 27

GPIO.setmode(GPIO.BCM)
count = 0.1

GPIO.setup(pin, GPIO.IN)
GPIO.add_event_detect(pin, GPIO.FALLING)

print 'Press the button!'

try:
  while True:
    global count
    if GPIO.event_detected(pin):
        print 'button pressed!!!'
        count = (count + 0.1) 
        sound.set_volume(count)
        print 'set sound',  count
        sound.play()

except KeyboardInterrupt:
    GPIO.cleanup()
