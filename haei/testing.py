import pyaudio

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
  dev = p.get_device_info_by_index(1)
  print((1,dev['name'], dev['maxInputChannels']))
