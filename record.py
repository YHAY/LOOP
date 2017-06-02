import pyaudio
import wave

CHK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output2.wav"

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
