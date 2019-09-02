# -*- coding: cp949 -*-
import pygame
import sys
import time
import pyaudio
import wave
import numpy as np
import glob
import os

CHK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

class loop():
    def __init__(self):

        self.count = 0;
        self.volume = 1;
        self.save_waves = {}
        self.out_stream = {}
        self.WAVE_OUTPUT_FILENAME = "output2.wav"
        self.RECORD_FILENAME = "record" + str(self.count) + ".wav"
        #path = '/home/haei/Music/'
        self.save_path = '/home/h/PycharmProjects/LOOP/LOOP/haei/'
        self.channel = pygame.mixer.find_channel()

    def record(self):
        global CHK
        global FORMAT
        global CHANNELS
        global RATE
        global RECORD_SECONDS
        p = pyaudio.PyAudio()
        if(self.count <5):
          print(self.count ,"* recording")

          in_stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHK)
          frames = []

          for i in range(0, int(RATE / CHK * RECORD_SECONDS)):
            data = in_stream.read(CHK)
            frames.append(data)

          print("* done recording")

          wf = wave.open(self.RECORD_FILENAME, 'wb')
          wf.setnchannels(CHANNELS)
          wf.setsampwidth(p.get_sample_size(FORMAT))
          wf.setframerate(RATE)
          wf.writeframes(b''.join(frames))
          wf.close()
          self.mixer()
          print("current:"+ self.RECORD_FILENAME)
          self.count +=1
          self.RECORD_FILENAME = "record"+str(self.count)+".wav"
          print ("next:"+ self.RECORD_FILENAME)
        else:
          print ("out of range! you can't record anymore. please save or restart all")

    def mixer(self):
        pygame.mixer.init()
        self.channel = pygame.mixer.find_channel()
        self.channel.play(pygame.mixer.Sound(self.RECORD_FILENAME),-1)

    def back(self):
        self.channel.stop()
        self.count -= 1
        print (self.RECORD_FILENAME + " is back")

        if(self.count<0):
            self.count=0
        self.RECORD_FILENAME = "record"+str(self.count)+".wav"
        print ("current:"+self.RECORD_FILENAME)
        fname=self.RECORD_FILENAME

        files = glob.glob("*")
        os.chdir(self.save_path)

        for f in files:
            if f ==fname:
               print ("!!!")
               os.remove(fname)
               print ("file name ["+f+"]")#show the remain lists

    def save(self):
        global CHK
        global FORMAT
        global CHANNELS
        global RATE
        global RECORD_SECONDS
        p = pyaudio.PyAudio()
        pygame.mixer.stop()

        frames = []
        wave_Files = []
        read_data = []
        data_to_int = []
        data = 0.0

        for i in range(0, self.count):
            wave_Files.append(wave.open("record" + str(i) + ".wav", 'rb'))
        # wf1 = wave.open(path+"record"+str(0)+".wav",'rb')
        # wf2 = wave.open(path+"record"+str(1)+".wav",'rb')#######

        # out_stream = p.open(format = p.get_format_from_width(wf2.getsampwidth()), channels = wf2.getnchannels(), rate = wf2.getframerate(), output = True)
        out_stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHK)

        for i in range(0, self.count):
            read_data.append(wave_Files[i].readframes(CHK))
        # data1 = wf1.readframes(chk)#######
        # data2 = wf2.readframes(chk)#######

        while (list([i for i in range(0, self.count) if read_data[i] != b''])):
        #while ((read_data[0] != b'') & (read_data[1] != b'')):
            # ((read_data[r_data] for r_data in range(0, count)) != b''):
            # print("r_data :", r_data)
            # ((read_data[] != b'') & (data2 != b'')):
            for i in range(0, self.count):
                out_stream.write(read_data[i])  ##########
                # out_stream.write(data2)##########
            for i in range(0, self.count):
                read_data[i] = wave_Files[i].readframes(CHK)
                # data1 = wf1.readframes(chk)#######
                # data2 = wf2.readframes(chk)##########
            for i in range(0, self.count):
                data_to_int.append(np.fromstring(read_data[i], np.int16))
                # d1 = np.fromstring(data1, np.int16)###########
                # d2 = np.fromstring(data2, np.int16)#############

                # data = (d1 * 0.333 + d2 * 0.333).astype(np.int16)############3
            data_sum = 0.0
            for j in range(0, self.count):
                data_sum += data_to_int[j] * (1 / self.count)

            data = data_sum.astype(np.int16)
            out_stream.write(data)  ###########
            print("data:", data)
            frames.append(data.tostring())  ###########33
            data_to_int.clear()

        print('all recording done')

        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        out_stream.stop_stream()
        out_stream.close()

    def delete(self):
        if (self.count >-1):
          print ('All deleting')
          pygame.mixer.stop()
          os.chdir(self.save_path)#go to the path
          files = glob.glob("record*") #find the file start with "record"
          for i in files: #  files : [record.py, record0.py...]
                  print ("!!!")
                  os.remove(i)
                  print ("file name ["+i+"]")#show the remain lists : empty= success

    def volume_up(self):
        self.volume = (self.volume + 0.1)
        self.channel.set_volume(self.volume)
        c=self.channel.get_volume()
        print ('set sound',  c, self.volume)

    def volume_down(self):
        self.volume = (self.volume - 0.1)
        self.channel.set_volume(self.volume)
        a=self.channel.get_volume()
        print ('set sound', a, self.volume)

if __name__ == "__main__":
    pygame.init()
    size = (200, 200)
    screen = pygame.display.set_mode(size)
    user_loop = loop()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_z:
                    user_loop.record()
                if event.key == pygame.K_x:
                    user_loop.back()
                if event.key == pygame.K_c:
                    user_loop.delete()
                if event.key == pygame.K_v:
                    user_loop.volume_up()
                if event.key == pygame.K_b:
                    user_loop.volume_down()
                if event.key == pygame.K_a:
                    user_loop.save()