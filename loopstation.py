import pygame
import sys
import RPi.GPIO as GPIO
import time
import pyaudio
import wave
import numpy as np

CHK = 1024
chk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

#naming rules : "outputs"+"count"+".py"


path = '/home/pi/loopproject'

count = 0;
savecnt = 0;
volume = 1;
deletecnt = 0

WAVE_OUTPUT_FILENAME = "music.wav"
RECORD_FILENAME = "record"+str(count)+".wav"

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

def record():
    global count
    print("* recording")

    in_stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,input=True, frames_per_buffer=CHK)
    
    frames = []

    for i in range(0, int(RATE / CHK * RECORD_SECONDS)):
      data = stream.read(CHK)
      frames.append(data)

    print("* done recording")
    
    wf = wave.open(RECORD_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    print("* recording")
    count +=1 

    
def mixer():
    pygame.mixer.init()
    channel = pygame.mixer.find_channel()
    channel.play(pygame.mixer.Sound(RECORD_FILENAME),-1)
    
    
def back():
    global count
    channel.stop()
    count -= 1
    files = glob.glob("*")
    os.chdir(path+RECORD_FILENAME)
    for f in files:
        if f ==fname:
         print "!!!"
         os.remove(fname)
         print "file name ["+f+"]"#show the remain lists

    

def delete():
    global deletecnt
    global count
    while(deletecnt > count): 
        files = glob.glob("*")
        os.chdir(path+"record"+count+".wav")
        for f in files:
             if f ==fname:
              print "!!!"
             os.remove(fname)
        #   print "file name ["+f+"]"#show the remain lists
        deletecnt+=1
        
def save():
    global savecnt
    global WAVE_OUTPUT_FILENAME
    global CHK 
    global chk
    global FORMAT 
    global CHANNELS 
    global RATE
    global RECORD_SECONDS 

    if savecnt == 0:
        out_stream = p.open(format = p.get_format_from_width(wf2.getsampwidth()), channels = wf2.getnchannels(), rate = wf2.getframerate(), output = True)

        wf1 = wave.open(path+"record"+0+".wav",rb)
        wf2 = wave.open(path+"record"+1+".wav",rb)

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

                data = (d2 * 0.333 + d3 * 0.333 + d4 * 0.333).astype(np.int16)
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
                wf1 = wave.open(path+"record"+str(savecnt)+".wav",rb)
                wf2 = wave.open(path+WAVE_OUTPUT_FILENAME,rb)

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

                        data = (d2 * 0.333 + d3 * 0.333 + d4 * 0.333).astype(np.int16)
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

    delete()     
             
    

def volume_up():
    global volume
    sound=pygame.mixer.Sound(RECORD_FILENAME)
    volume = (volume + 0.1) 
    sound.set_volume(volume)
    print 'set sound',  volume


def volume_down():
    global volume
    sound=pygame.mixer.Sound(RECORD_FILENAME)
    volume = (volume - 0.1) 
    sound.set_volume(volume)
    print 'set sound',  volume

###GPIO settings###
#vol_up
GPIO.setup(vol_up, GPIO.IN)
GPIO.add_event_detect(vol_up, GPIO.FALLING, callback = volume_up, bouncetime=1)
#vol_down
GPIO.setup(vol_down, GPIO.IN)
GPIO.add_event_detect(vol_down, GPIO.FALLING, callback = volume_down, bouncetime=1)
#save
GPIO.setup(save_pin, GPIO.IN)
GPIO.add_event_detect(save_pin, GPIO.FALLING, callback = save, bouncetime=1)
#record
GPIO.setup(rec_pin, GPIO.IN)
GPIO.add_event_detect(rec_pin, GPIO.FALLING,callback = record, bouncetime=1)
#back
GPIO.setup(back_pin, GPIO.IN)
GPIO.add_event_detect(back_pin, GPIO.FALLING, callback = back, bouncetime=1)
#delete
GPIO.setup(del_pin, GPIO.IN)
GPIO.add_event_detect(del_pin, GPIO.FALLING, callback = delete, bouncetime =1)

print 'Press the button!'
frames = []

try:
  while True:
   time.sleep(1)
	
except KeyboardInterrupt:
    GPIO.cleanup()
