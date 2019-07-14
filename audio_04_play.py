import sys
import pyaudio
import wave

import pygame

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 3

def play_wav(file_name):
    wf = wave.open(file_name, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)
    data = wf.readframes(CHUNK)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
    p.terminate()

def play_mp3(file_name):
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()
    while True:
        if not pygame.mixer.music.get_busy():
            sys.exit()


if __name__ == '__main__':
    # play_wav('output.wav')
    play_mp3('result.mp3')