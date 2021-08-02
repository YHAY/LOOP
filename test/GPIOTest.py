import os
import glob
import wave
import pygame
import pyaudio
import numpy as np
import RPi.GPIO as GPIO


CHK = 1024
chk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

#naming rules : "outputs"+"count"+".py"
todir="/home/pi/sound/"
WAVE_OUTPUT_FILENAME = "outputs.wav"
NEW_WAVE_OUTPUT_FILENAME = "new_outputs.wav"

path1 = '/home/pi/LOOP/LOOP/haei/output1.wav'
path2 = '/home/pi/LOOP/LOOP/haei/output2.wav'
path3 = '/home/pi/LOOP/LOOP/haei/output3.wav'


#PIN LIST
vol_up = 13
vol_down = 19
save_pin = 6
rec_pin = 27
back_pin = 5
del_pin = 23

#GPIO setmode
GPIO.setmode(GPIO.BCM)
#pygame init
pygame.init()
#pyaudio init
p = pyaudio.PyAudio()

###GPIO settings###
#vol_up
GPIO.setup(vol_up, GPIO.IN)
GPIO.add_event_detect(vol_up, GPIO.FALLING)
#vol_down
GPIO.setup(vol_down, GPIO.IN)
GPIO.add_event_detect(vol_down, GPIO.FALLING)
#save
GPIO.setup(save_pin, GPIO.IN)
GPIO.add_event_detect(save_pin, GPIO.FALLING)
#record
GPIO.setup(rec_pin, GPIO.IN)
GPIO.add_event_detect(rec_pin, GPIO.FALLING)
#back
GPIO.setup(back_pin, GPIO.IN)
GPIO.add_event_detect(back_pin, GPIO.FALLING)
#delete
GPIO.setup(del_pin, GPIO.IN)
GPIO.add_event_detect(del_pin, GPIO.FALLING)

print('Press the button!')
frames = []
try:
  while True:
    if GPIO.event_detected(rec_pin):
        print("* recording")
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,input=True, frames_per_buffer=CHK)
        for i in range(0, int(RATE / CHK * RECORD_SECONDS)):
            data = stream.read(CHK)
            frames.append(data)

        if count !=0:
            wf2 = wave.open((todir+NEW_WAVE_OUTPUT_FILENAME), 'rb')
            out_stream = p.open(format = p.get_format_from_width(wf2.getsampwidth()), channels = wf2.getnchannels(), rate = wf2.getframerate(), output = True)
            data2 = wf2.readframes(chk)
            while data2 != '' :
                out_stream.write(data2)#for play
                data2 = wf2.readframes(chk)#for play
                d2 = np.fromstring(data2, np.int16)
                 #data = (d2 * 0.333 + d3 * 0.333 + d4 * 0.333).astype(np.int16)
                 out_stream.write(data)
                 frames.append(data.tostring())
        print ('all recording done')
        wf = wave.open(NEW_WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        p.terminate()

        break
    if GPIO.event_detected(del_pin):
        files = glob.glob("*")
        os.chdir(todir)
        for f in files:
          if f ==fname:
            print ("!!!")
            os.remove(fname)
          print ("file name ["+f+"]")#show the remain lists
          break

    if GPIO.event_detected(back_pin):
        print ('back_pin pressed')
        break
    if GPIO.event_detected(save_pin):
        print ('save_pin pressed')
        break
    if GPIO.event_detected(vol_up):
        print ('vol_up pressed')
        break
    if GPIO.event_detected(vol_down):
        print ('vol_down pressed')
        break

except KeyboardInterrupt:
    GPIO.cleanup()
