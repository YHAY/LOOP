import RPi.GPIO as GPIO
import time
import pyaudio
import wave


p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,input=True, frames_per_buffer=CHK)

GPIO.setmode(GPIO.BCM)
count = 0
def handler(channel):
    global count
    count = count + 1
    print count
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(24, GPIO.RISING, callback=handler)
try:  
    GPIO.wait_for_edge(23, GPIO.FALLING)
    print "Falling edge detected."
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL_C
GPIO.cleanup()
