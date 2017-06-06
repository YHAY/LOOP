# -*- coding: cp949 -*-
import pygame
import sys
import time
import pyaudio
import wave
import numpy as np
import glob
import os

chk = 2048
CHK =  2048
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

count = 0;
savecnt = 0;
volume = 1;
deletecnt = 0

p = pyaudio.PyAudio()

pygame.init()
size = (200, 200)
screen = pygame.display.set_mode(size)

WAVE_OUTPUT_FILENAME = "output.wav"
RECORD_FILENAME = "record"+str(count)+".wav"
path = '/home/haei/Music/haei/'
channel = pygame.mixer.find_channel()


def record():
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

    global channel
    global count
    global RECORD_FILENAME
    channel.stop()
    
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
'''
def delete():

    global RECORD_FILENAME
    global count
    

    print RECORD_FILENAME
    pygame.mixer.stop()

    while(count>0):
        count-=1 
        RECORD_FILENAME = "record"+str(count)+".wav"
        files = glob.glob("*")
        os.chdir(path)
        fname=RECORD_FILENAME
        for f in files:
             if f ==fname:
              print "!!!"
             os.remove(fname)   
        #   print "file name ["+f+"]"#show the remain lists
'''
def save():
    print("click")
    global savecnt
    global WAVE_OUTPUT_FILENAME
    global CHK 
    global chk
    global FORMAT 
    global CHANNELS 
    global RATE
    global RECORD_SECONDS 

    pygame.mixer.stop()
    
    if savecnt == 0:

        wf1 = wave.open(path+"record"+str(0)+".wav",'rb')
        wf2 = wave.open(path+"record"+str(1)+".wav",'rb')
        
        out_stream = p.open(format = p.get_format_from_width(wf2.getsampwidth()), channels = wf2.getnchannels(), rate = wf2.getframerate(), output = True)
        frames = []
        data1 = wf1.readframes(chk)
        data2 = wf2.readframes(chk)

        while data1 != '' :
            if data2 != '':
                out_stream.write(data1)
                out_stream.write(data2)
                
                data1 = wf1.readframes(chk)
                data2 = wf2.readframes(chk)
        
                d1 = np.fromstring(data1, np.int16)
                d2 = np.fromstring(data2, np.int16)

                data = (d1 * 0.333 + d2 * 0.333).astype(np.int16)
                out_stream.write(data)
                          
                frames.append(data.tostring())
                
        print 'all recording done'

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        out_stream.stop_stream()
        out_stream.close()
                
        savecnt += 1

        if savecnt > 0:
             while savecnt == count:
                wf1 = wave.open(path+"record"+str(savecnt)+".wav",'rb')
                wf2 = wave.open(path+WAVE_OUTPUT_FILENAME,'rb')

                data1 = wf1.readframes(chk)
                data2 = wf2.readframes(chk)
                
                while data1 != '' :
                    if data2 != '':
                        out_stream.write(data1)
                        out_stream.write(data2)
                        
                        data1 = wf1.readframes(chk)
                        data2 = wf2.readframes(chk)
                
                        d1 = np.fromstring(data1, np.int16)
                        d2 = np.fromstring(data2, np.int16)

                        data = (d1 * 0.333 + d2 * 0.333).astype(np.int16)
                        out_stream.write(data)
                                  
                        frames.append(data.tostring())
                        
                        print 'all recording done'
                        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
                        wf.setnchannels(CHANNELS)
                        wf.setsampwidth(p.get_sample_size(FORMAT))
                        wf.setframerate(RATE)
                        wf.writeframes(b''.join(frames))
                        wf.close()
                        
                        out_stream.stop_stream()
                        out_stream.close()
             savecnt += 1

def delete():
    if (count >-1):
      print 'All deleting'
      pygame.mixer.stop()
      os.chdir(path)#go to the path
      files = glob.glob("record*") #find the file start with "record"
      for i in files: #  files : [record.py, record0.py...]
              print "!!!"
              os.remove(i)
              print "file name ["+i+"]"#show the remain lists : empty= success
             
    

def volume_up():
    global volume
    global channel
    volume = (volume + 0.1) 
    channel.set_volume(volume)
    c=channel.get_volume()
    print 'set sound',  c,volume


def volume_down():
    global volume
    global channel
    volume = (volume - 0.1) 
    channel.set_volume(volume)
    a=channel.get_volume()
    print 'set sound', a,volume


while True:


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_z:
                record()          
            if event.key == pygame.K_x:
                back()
            if event.key == pygame.K_c:
                delete()
            if event.key == pygame.K_v:
                volume_up()
            if event.key == pygame.K_b:
                volume_down()
            if event.key == pygame.K_a:
                save()
       
               


