import pyaudio
import wave
import sys

chk = 2048

if len(sys.argv) < 2:
  print("plays a wave file. \n\n usage: %s filename.wav" % sys.argv[0])
  sys.exit(-1)

wf = wave.open(sys.argv[1],'rb')

p = pyaudio.PyAudio()

stream = p.open(format = p.get_format_from_width(wf.getsampwidth()), channels = wf.getnchannels(), rate = wf.getframerate(), output = True)

data = wf.readframes(chk)

while data != '':
  stream.write(data)
  data = wf.readframes(chk)

stream.stop_stream()
stream.close()

p.terminate()
