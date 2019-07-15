import threading

import pyaudio
import wave

CHUNK = 1024  # 数据流块
FORMAT = pyaudio.paInt16  # 音频格式
CHANNELS = 1  # 声道
RATE = 16000  # 码率
RECORD_SECONDS = 3  # 录制时长

def audio_record(wave_output_filename='output.wav'):
    """
    录制音频
    :param wave_output_filename: 输出的音频文件
    :return:
    """
    p = pyaudio.PyAudio()  # 创建音频对象

    # 打开数据流
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("开始录制")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)  # 读取数据
        frames.append(data)  # 添加到列表

    print("录制结束")

    stream.stop_stream()  # 停止数据流
    stream.close()  # 关闭流
    p.terminate()  # 关闭音频对象

    wf = wave.open(wave_output_filename, 'wb')  # 输出到音频文件
    wf.setnchannels(CHANNELS)  # 设置声道
    wf.setsampwidth(p.get_sample_size(FORMAT))  # 设置音频格式
    wf.setframerate(RATE)  # 设置音频码率
    wf.writeframes(b''.join(frames))  # 拼接字节流
    wf.close()  # 关闭输出流

if __name__ == '__main__':
    threading.Thread(target=audio_record, args=('output.wav',)).start()
