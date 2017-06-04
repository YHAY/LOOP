import pyaudio
import wave
import pygame
import time

CHK = 2**12
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 3

count = 0;

p = pyaudio.PyAudio()

size = (200, 200)
screen = pygame.display.set_mode(size)

while True:
    if count >= 1:
      print ("play")
      pygame.mixer.init()
      sound = "rctest"+str(count)+".wav"
      channel = pygame.mixer.find_channel()
      channel.play(pygame.mixer.Sound(sound),-1)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            
            if event.key == pygame.K_r:
                print("* recording")
                
                frames = []
                stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,input=True, frames_per_buffer=CHK)
                for i in range(0, int(RATE / CHK * RECORD_SECONDS)):
                  data = stream.read(CHK)
                  frames.append(data)
                print("* done recording")
                
                count +=1
  
                if(count >= 1) :
                      wf = wave.open("rctest"+str(count)+".wav",'wb')
                      wf.setnchannels(CHANNELS)
                      wf.setsampwidth(p.get_sample_size(FORMAT))
                      wf.setframerate(RATE)
                      wf.writeframes(b''.join(frames))
                      wf.close()
                     
            
            if event.key == pygame.K_q:
               print ("stop"+count+"music") 
               chnnel[count].stop();
               count -= 1;
