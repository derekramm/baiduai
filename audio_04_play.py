import sys
import pyaudio
import wave
import pygame

CHUNK = 1024  # 数据流块
FORMAT = pyaudio.paInt16  # 音频格式
CHANNELS = 1  # 声道
RATE = 16000  # 码率
RECORD_SECONDS = 3  # 录制时长

def play_wav(wave_output_filename='output.wav'):
    """
    播放音频文件
    :param wave_output_filename: 音频文件名
    :return:
    """
    wf = wave.open(wave_output_filename, 'rb')  # 打开音频文件
    p = pyaudio.PyAudio()  # 创建音频对象

    # 打开数据流
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)
    # 读取音频流
    data = wf.readframes(CHUNK)

    # 如果读到的流长度大于0，持续输出到流
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

    # 停止流
    stream.stop_stream()
    # 关闭流
    stream.close()
    # 关闭音频对象
    p.terminate()

def play_mp3(wave_output_filename='result.mp3'):
    # 初始化音频对象
    pygame.mixer.init()
    # 加载指定的音频文件
    pygame.mixer.music.load(wave_output_filename)
    # 播放音频文件
    pygame.mixer.music.play()
    # 监听
    while True:
        # 如果读取结束
        if not pygame.mixer.music.get_busy():
            break  # 终止程序

if __name__ == '__main__':
    # play_wav('output.wav')
    # play_mp3('result.mp3')
    pass
