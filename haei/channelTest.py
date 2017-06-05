import pygame
import sys
import pyaudio
import wave
import numpy as np

pygame.init()
size = (200, 200)
screen = pygame.display.set_mode(size)
LEFT = 1

CHK = 1024
chk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "outputs.wav"
NEW_WAVE_OUTPUT_FILENAME = "new_outputs.wav"

path1 = '/home/pi/LOOP/LOOP/haei/output1.wav'
path2 = '/home/pi/LOOP/LOOP/haei/output2.wav'
path3 = '/home/pi/LOOP/LOOP/haei/output3.wav'

s = pygame.mixer.Sound("test2.wav")
s2 = pygame.mixer.Sound("test1.wav")

p = pyaudio.PyAudio()


#stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,input=True, frames_per_buffer=CHK)

#frames = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("* recording")

                frames = []

                in_stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,input=True, frames_per_buffer=CHK)

                wf2 = wave.open(path1, 'rb')
                out_stream = p.open(format = p.get_format_from_width(wf2.getsampwidth()), channels = wf2.getnchannels(), rate = wf2.getframerate(), output = True)


                '''
                for i in range(0, int(RATE / CHK * RECORD_SECONDS)):
                    data = in_stream.read(CHK)
                    frames.append(data)
                print("* recording done")
                wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(p.get_sample_size(FORMAT))
                wf.setframerate(RATE)
                wf.writeframes(b''.join(frames))
                wf.close()
		'''
                wf3 = wave.open(path2, 'rb')
                wf4 = wave.open(path3, 'rb')

                data2 = wf2.readframes(chk)
                data3 = wf3.readframes(chk)
                data4 = wf4.readframes(chk)                		

                print len(data2), len(data3), len(data4)
                print df2, df3, df4
                print cf2, cf3, cf4
                print sf2, sf3, sf4
                while data2 != '' :
                  if data3 != '':
                    if data4 !='':
                      out_stream.write(data2)
                      out_stream.write(data3)
                      out_stream.write(data4)
                      data2 = wf2.readframes(chk)
                      data3 = wf3.readframes(chk)
                      data4 = wf4.readframes(chk)
    
                      d2 = np.fromstring(data2, np.int16)
                      d3 = np.fromstring(data3, np.int16)
                      d4 = np.fromstring(data4, np.int16)
                      print len(d2), len(d3), len(d4)
                      data = (d2 * 0.333 + d3 * 0.333 + d4 * 0.333).astype(np.int16)
                      out_stream.write(data)
                      
                      frames.append(data.tostring())

                print 'all recording done'
		wf = wave.open(NEW_WAVE_OUTPUT_FILENAME, 'wb')
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(p.get_sample_size(FORMAT))
                wf.setframerate(RATE)
                wf.writeframes(b''.join(frames))
                wf.close()
                
                out_stream.stop_stream()
                out_stream.close()

                p.terminate()
                pygame.mixer.music.load(NEW_WAVE_OUTPUT_FILENAME)
                pygame.mixer.music.play()
                break

            if event.key == pygame.K_b:
                print "click bbb"
                pygame.mixer.music.load(WAVE_OUTPUT_FILENAME)
                pygame.mixer.music.queue(path2)
            if event.key == pygame.K_c:
                print "click ccc"
                pygame.mixer.music.play()

