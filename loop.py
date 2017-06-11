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

#p = pyaudio.PyAudio()

pygame.init()
size = (200, 200)
screen = pygame.display.set_mode(size)

#WAVE_OUTPUT_FILENAME = "output.wav"
WAVE_OUTPUT_FILENAME = "output2.wav"
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
    p = pyaudio.PyAudio()
    if(count <5):
      print(count ,"* recording")

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
    else:
      print "out of range! you can't record anymore. please save or restart all"

    
def mixer():
    pygame.mixer.init()
    channel = pygame.mixer.find_channel()
    channel.play(pygame.mixer.Sound(RECORD_FILENAME),-1)

#####################################################################
def back():
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


def save():
    print("click")
    global count
#    global savecnt
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


################################################
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



################################################
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
       
               



