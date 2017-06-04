import pygame
import sys
import pyaudio
import wave

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
path1 = '/home/haei/Music/haei/test2.wav'
path2 = '/home/haei/Music/haei/test1.wav'

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
                stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,input=True, frames_per_buffer=CHK)
                frames = []
                '''
                for i in range(0, int(RATE / CHK * RECORD_SECONDS)):
                    data = stream.read(CHK)
                    frames.append(data)
                print("* recording done")
                wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(p.get_sample_size(FORMAT))
                wf.setframerate(RATE)
                wf.writeframes(b''.join(frames))
                wf.close()
                '''
                wf2 = wave.open(path1, 'rb')
                wf3 = wave.open(path2, 'rb')
                

                stream = p.open(format = p.get_format_from_width(wf2.getsampwidth()), channels = wf2.getnchannels(), rate = wf2.getframerate(), output = True)
                data2 = wf2.readframes(chk)
                data3 = wf3.readframes(chk)
		
                while data2 != '' :
                  if data3 != '':
                    stream.write(data2)
                    stream.write(data3)
                    data2 = wf2.readframes(chk)
                    data3 = wf3.readframes(chk)
                    frames.append(data2)
                    frames.append(data3)

                print 'recording done'
		wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(p.get_sample_size(FORMAT))
                wf.setframerate(RATE)
                wf.writeframes(b''.join(frames))
                wf.close()
                
                stream.stop_stream()
                stream.close()

                p.terminate()
                #pygame.mixer.music.load(WAVE_OUTPUT_FILENAME)
                #pygame.mixer.music.play()
                break

            if event.key == pygame.K_b:
                print "click bbb"
                pygame.mixer.music.load(WAVE_OUTPUT_FILENAME)
                pygame.mixer.music.queue(path2)
            if event.key == pygame.K_c:
                print "click ccc"
                pygame.mixer.music.play()

