import pygame
import sys
import time
import pyaudio
import wave
import numpy as np
import glob
import os
import RPi.GPIO as GPIO
from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep

chk = 2**12
CHK =  2**12
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10

#PIN LIST
vol_up = 13
vol_down = 19
save_pin = 6
rec_pin = 27
back_pin = 5
del_pin = 23

count = 0;
savecnt = 1;
volume = 1;
deletecnt = 0

p = pyaudio.PyAudio()

pygame.init()

GPIO.setmode(GPIO.BCM)

WAVE_OUTPUT_FILENAME = "output.wav"
RECORD_FILENAME = "record"+str(count)+".wav"
path = '/home/pi/loopproject/'
channel = pygame.mixer.find_channel()


def record():
    lcds()
    global count
    global RECORD_FILENAME
    global WAVE_OUTPUT_FILENAME
    global CHK 
    global FORMAT 
    global CHANNELS 
    global RATE
    global RECORD_SECONDS 
    print("* recording")

    in_stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,input=True, frames_per_buffer=CHK)
    
    frames = []

    for i in range(0, int(RATE / CHK * RECORD_SECONDS)):
      data = in_stream.read(CHK)
      frames.append(data)

    in_stream.close()
    print("* done recording")
    
    wf = wave.open(RECORD_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    mixer()
    print"current:"+ RECORD_FILENAME
    count +=1
    RECORD_FILENAME = "record"+str(count)+".wav"
    print "next:"+RECORD_FILENAME

    
def mixer():
    
    pygame.mixer.init()
    channel = pygame.mixer.find_channel()
    channel.play(pygame.mixer.Sound(RECORD_FILENAME),-1)

    
    
def back():
    lcds()
    global channel
    global count
    global RECORD_FILENAME

    pygame.mixer.stop()


    count -= 1
    print RECORD_FILENAME + "is back"
    
    if(count<0):
        count=0
    RECORD_FILENAME = "record"+str(count)+".wav"
    print "current:"+RECORD_FILENAME
    fname=RECORD_FILENAME

    files = glob.glob("*")
    os.chdir(path)

    for f in files:
        if f ==fname:
         print "!!!"
         os.remove(fname)
         print "file name ["+f+"]"#show the remain lists
    
    for j in range(0,count):
      channel = pygame.mixer.find_channel()
      RECORD_FILENAME = "record"+str(j)+".wav"
      print "current:"+RECORD_FILENAME
      fname=RECORD_FILENAME
      channel.play(pygame.mixer.Sound(fname), -1)
      
def delete():
    lcds()
    global count
    if (count >-1):
        print 'All deleting'
        pygame.mixer.stop()
        os.chdir(path)#go to the path
        files = glob.glob("record*") #find the file start with "record"
        for i in files: #  files : [record.py, record0.py...]
              print "!!!"
              os.remove(i)
              print "file name ["+i+"]"#show the remain lists : empty= success
        count=0

def save():
    print("click")
    global count
    global WAVE_OUTPUT_FILENAME
    global CHK 
    global chk
    global FORMAT 
    global CHANNELS 
    global RATE
    global RECORD_SECONDS
    p = pyaudio.PyAudio()
    
    pygame.mixer.stop()
    # 4 sounds
    
    if count == 1:
        print("count = 1")
        frames = []
        wf1 = wave.open(path+"record"+str(0)+".wav",'rb')#######
        out_stream = p.open(format = p.get_format_from_width(wf2.getsampwidth()), channels = wf2.getnchannels(), rate = wf2.getframerate(), output = True)
        data1 = wf1.readframes(chk)#######

        while data1 != '' :
            if data2 != '':
                out_stream.write(data1)##########
                data1 = wf1.readframes(chk)#######

                d1 = np.fromstring(data1, np.int16)###########
                data = (d1).astype(np.int16)
                out_stream.write(data)###########

                frames.append(data.tostring())###########33
        print 'all recording done'

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        out_stream.stop_stream()
        out_stream.close()

    if count == 2:
        print("count = 2")
        frames = []
        wf1 = wave.open(path+"record"+str(0)+".wav",'rb')#######
        wf2 = wave.open(path+"record"+str(1)+".wav",'rb')#######
        
        out_stream = p.open(format = p.get_format_from_width(wf2.getsampwidth()), channels = wf2.getnchannels(), rate = wf2.getframerate(), output = True)

        data1 = wf1.readframes(chk)#######
        data2 = wf2.readframes(chk)#######

        while data1 != '' :
            if data2 != '':
                out_stream.write(data1)##########
                out_stream.write(data2)##########
                
                data1 = wf1.readframes(chk)#######
                data2 = wf2.readframes(chk)##########
        
                d1 = np.fromstring(data1, np.int16)###########
                d2 = np.fromstring(data2, np.int16)#############

                #data = (d1 * 0.333 + d2 * 0.333).astype(np.int16)############3
                data = (d1 * 0.5 + d2 * 0.5).astype(np.int16)
                out_stream.write(data)###########
                          
                frames.append(data.tostring())###########33
                
        print 'all recording done'

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        out_stream.stop_stream()
        out_stream.close()

    if count == 3:
        print("count = 3")
        frames = []
        wf1 = wave.open(path+"record"+str(0)+".wav",'rb')#######
        wf2 = wave.open(path+"record"+str(1)+".wav",'rb')#######z
        wf3 = wave.open(path+"record"+str(2)+".wav",'rb')#######z
        
        out_stream = p.open(format = p.get_format_from_width(wf2.getsampwidth()), channels = wf2.getnchannels(), rate = wf2.getframerate(), output = True)

        data1 = wf1.readframes(chk)#######
        data2 = wf2.readframes(chk)#######
        data3 = wf3.readframes(chk)#######

        while data1 != '' :
            if data2 != '':
              if data3 != '':
                out_stream.write(data1)##########
                out_stream.write(data2)##########
                out_stream.write(data3)##########
                
                data1 = wf1.readframes(chk)#######
                data2 = wf2.readframes(chk)##########
                data3 = wf3.readframes(chk)##########
        
                d1 = np.fromstring(data1, np.int16)###########
                d2 = np.fromstring(data2, np.int16)#############
                d3 = np.fromstring(data3, np.int16)#############

                data = (d1 * 0.333 + d2 * 0.333 + d3 * 0.333).astype(np.int16)############3
                out_stream.write(data)###########
                frames.append(data.tostring())###########33
                
        print 'all recording done'

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        out_stream.stop_stream()
        out_stream.close()

    if count == 4:
        print("count = 4")
        frames = []
        wf1 = wave.open(path+"record"+str(0)+".wav",'rb')#######
        wf2 = wave.open(path+"record"+str(1)+".wav",'rb')#######
        wf3 = wave.open(path+"record"+str(2)+".wav",'rb')#######
        wf4 = wave.open(path+"record"+str(3)+".wav",'rb')#######
        

        out_stream = p.open(format = p.get_format_from_width(wf2.getsampwidth()), channels = wf2.getnchannels(), rate = wf2.getframerate(), output = True)

        data1 = wf1.readframes(chk)#######
        data2 = wf2.readframes(chk)#######
        data3 = wf3.readframes(chk)#######
        data4 = wf4.readframes(chk)#######

        while data1 != '' :
            if data2 != '':
              if data3 != '':
                if data4 != '':
                  out_stream.write(data1)##########
                  out_stream.write(data2)##########
                  out_stream.write(data3)##########
                  out_stream.write(data4)##########
                
                  data1 = wf1.readframes(chk)#######
                  data2 = wf2.readframes(chk)##########
                  data3 = wf3.readframes(chk)#######
                  data4 = wf4.readframes(chk)##########
        
                  d1 = np.fromstring(data1, np.int16)###########
                  d2 = np.fromstring(data2, np.int16)#############
                  d3 = np.fromstring(data3, np.int16)###########
                  d4 = np.fromstring(data4, np.int16)#############

                  data = (d1 * 0.25 + d2 * 0.25 + d3 * 0.25 + d4 * 0.25 ).astype(np.int16)############3
                  out_stream.write(data)###########
                          
                  frames.append(data.tostring())###########33
                
        print 'all recording done'

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        out_stream.stop_stream()
        out_stream.close()
    else:
        print 'recording num is out of range. please press again'
        count = 4
   # delete()     
             
    

def volume_up():
    global volume
    global channel
    pygame.mixer.stop()

    for j in range(0,count):
      channel = pygame.mixer.find_channel()
      RECORD_FILENAME = "record"+str(j)+".wav"
      print "current:"+RECORD_FILENAME
      fname=RECORD_FILENAME
      channel.play(pygame.mixer.Sound(RECORD_FILENAME),-1)
      volume = (volume + 0.1)
      channel.set_volume(volume)
      c=channel.get_volume()
      print 'set sound',  c,volume

def volume_down():
    global volume
    global channel
    pygame.mixer.stop()


    for j in range(0,count):
      channel = pygame.mixer.find_channel()
      RECORD_FILENAME = "record"+str(j)+".wav"
      print "current:"+RECORD_FILENAME
      fname=RECORD_FILENAME
      volume = (volume - 0.1)
      channel.set_volume(volume)

      channel.play(pygame.mixer.Sound(RECORD_FILENAME),-1)
      a=channel.get_volume()
      print 'set sound', a,volume

    
GPIO.setup(vol_up, GPIO.IN)
GPIO.add_event_detect(vol_up, GPIO.FALLING,bouncetime=300)
#vol_down
GPIO.setup(vol_down, GPIO.IN)
GPIO.add_event_detect(vol_down, GPIO.FALLING,bouncetime=300)
#save
GPIO.setup(save_pin, GPIO.IN)
GPIO.add_event_detect(save_pin, GPIO.FALLING,bouncetime=300)
#record
GPIO.setup(rec_pin, GPIO.IN)
GPIO.add_event_detect(rec_pin, GPIO.FALLING,bouncetime=300)
#back
GPIO.setup(back_pin, GPIO.IN)
GPIO.add_event_detect(back_pin, GPIO.FALLING,bouncetime=300)
#delete
GPIO.setup(del_pin, GPIO.IN)
GPIO.add_event_detect(del_pin, GPIO.FALLING,bouncetime=300)

def lcds():
        lcd = Adafruit_CharLCD(rs=22, en=11, d4=23, d5=10, d6=9, d7=25, cols=16, lines=2)
        lcd.clear()
        lcd.message(str(count) + 'st Recording')

print 'Press the button!'
frames = []

try:
    while True:

        if GPIO.event_detected(rec_pin):
            record()
            sleep(1)  
        if GPIO.event_detected(del_pin):
            delete()
            sleep(1) 
        if GPIO.event_detected(back_pin):
            back()
            sleep(1) 
        if GPIO.event_detected(save_pin):
            save()
            sleep(1) 
        if GPIO.event_detected(vol_up):
            volume_up()
            sleep(1) 
        if GPIO.event_detected(vol_down):
            volume_down()
            sleep(1) 


except KeyboardInterrupt:
    GPIO.cleanup()
