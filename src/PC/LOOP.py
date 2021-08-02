# -*- coding: cp949 -*-
import os
import glob
import wave
import pygame
import pyaudio
import numpy as np
from pathlib import Path

CHK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

'''
Todos,
1. music saved path automatically.(ok)
2. attach comment(ok)
3. remove print(ok) error control(ok)
5. clean the github. (divide it as PC/Raspberry) (ok)
4. write how to play this program. (ing) -> readme.md
6. refactoring PC code
7. test PC code
8. refactoring raspberry code
6. move it to raspberry. and test it. (with hw)
'''


class Loop:
    def __init__(self):
        self.count = 0
        self.volume = 1
        self.save_waves = {}
        self.out_stream = {}
        self.WAVE_OUTPUT_FILENAME = "result.wav"
        self.RECORD_FILENAME = "record" + str(self.count) + ".wav"
        home = str(Path.home())
        self.save_path = home + '/sound/'
        self.channel = pygame.mixer.find_channel()
        pygame.init()

    ''' Record a sound'''

    def record(self):
        # global CHK
        # global FORMAT
        # global CHANNELS
        # global RATE
        # global RECORD_SECONDS
        p = pyaudio.PyAudio()
        if self.count < 5:
            in_stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHK)
            frames = []

            for i in range(0, int(RATE / CHK * RECORD_SECONDS)):
                data = in_stream.read(CHK)
                frames.append(data)

            wf = wave.open(self.save_path + self.RECORD_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
            self.mixer()
            self.count += 1
            self.RECORD_FILENAME = "record" + str(self.count) + ".wav"
        else:
            raise Exception("out of save range! you can't record anymore. please save or restart all")

    ''' Keep play the sound that you record. It used in Record() function.'''

    def mixer(self):
        pygame.mixer.init()
        self.channel = pygame.mixer.find_channel()
        self.channel.play(pygame.mixer.Sound(self.save_path + self.RECORD_FILENAME), -1)

    ''' Remove '''

    def back(self):
        self.channel.stop()
        self.count -= 1

        if self.count < 0:
            self.count = 0
        self.RECORD_FILENAME = "record" + str(self.count) + ".wav"
        fname = self.RECORD_FILENAME

        files = glob.glob("*")
        os.chdir(self.save_path)

        for f in files:
            if f == fname:
                os.remove(fname)

    ''' Save a music with Combine '''

    def save(self):
        # global CHK
        # global FORMAT
        # global CHANNELS
        # global RATE
        # global RECORD_SECONDS
        p = pyaudio.PyAudio()
        pygame.mixer.stop()

        frames = []
        wave_files = []
        read_data = []
        data_to_int = []
        # data = 0.0

        for i in range(0, self.count):
            wave_files.append(wave.open("record" + str(i) + ".wav", 'rb'))
        out_stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHK)

        for i in range(0, self.count):
            read_data.append(wave_files[i].readframes(CHK))

        while list([i for i in range(0, self.count) if read_data[i] != b'']):
            for i in range(0, self.count):
                out_stream.write(read_data[i])
            for i in range(0, self.count):
                read_data[i] = wave_files[i].readframes(CHK)
            for i in range(0, self.count):
                data_to_int.append(np.fromstring(read_data[i], np.int16))
            data_sum = 0.0
            for j in range(0, self.count):
                data_sum += data_to_int[j] * (1 / self.count)

            data = data_sum.astype(np.int16)
            out_stream.write(data)
            frames.append(data.tostring())
            data_to_int.clear()

        wf = wave.open(self.save_path + self.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        out_stream.stop_stream()
        out_stream.close()

    ''' delete all files , start with "record" '''

    def delete(self):
        if self.count > -1:
            pygame.mixer.stop()
            os.chdir(self.save_path)
            files = glob.glob("record*")
            for i in files:
                os.remove(i)

    def volume_up(self):
        self.volume = (self.volume + 0.1)
        self.channel.set_volume(self.volume)
        self.channel.get_volume()

    def volume_down(self):
        self.volume = (self.volume - 0.1)
        self.channel.set_volume(self.volume)
        self.channel.get_volume()


if __name__ == "__main__":
    # create a square to get key input
    pygame.init()
    size = (200, 200)
    screen = pygame.display.set_mode(size)

    user_loop = Loop()  # create class.

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
