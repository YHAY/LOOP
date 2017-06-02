import RPi.GPIO as GPIO
import time
import pyaudio
import wave

CHK = 2
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output2.wav"

GPIO.setmode(GPIO.BCM)
count = 0

p = pyaudio.PyAudio()

GPIO.setup(23, GPIO.IN)
GPIO.add_event_detect(23, GPIO.FALLING)

GPIO.setup(27, GPIO.IN)
GPIO.add_event_detect(27, GPIO.FALLING)

print 'Press the button!'
frames = []
try:
  while True:
    if GPIO.event_detected(27):
        print("* recording")
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,input=True, frames_per_buffer=CHK)
        for i in range(0, int(RATE / CHK * RECORD_SECONDS)):
            data = stream.read(CHK)
            frames.append(data)

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        break
    if GPIO.event_detected(23):
        

except KeyboardInterrupt:
    GPIO.cleanup()
