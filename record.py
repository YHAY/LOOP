import pyaudio
import wave
import pygame
import time


CHK = 2**12
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"


p = pyaudio.PyAudio()

stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,input=True, frames_per_buffer=CHK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHK * RECORD_SECONDS)):
  data = stream.read(CHK)
  frames.append(data)

print("* done recording")
if 0xFF ==ord('q'):
  stream.stop_stream()
  stream.close()
  p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

time.sleep(2)
pygame.mixer.init()

S = pygame.mixer.Sound(WAVE_OUTPUT_FILENAME)
S.play();
while True:
  pass



