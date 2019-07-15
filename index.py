import threading
from audio_01_record import audio_record
from audio_04_play import play_mp3, play_wav
from audio_02_recognize import audio_recognize

if __name__ == '__main__':
    while True:
        input('请按任意键录音')

        # 录音
        record = threading.Thread(target=audio_record, args=('output.wav',))
        record.start()
        record.join()

        # 播放录制的音频文件
        play = threading.Thread(target=play_wav, args=('output.wav',))
        play.start()
        play.join()

        # 识别音频文件，将识别出的语音转换成文本，再发送给图灵机器人
        # 将图灵机器人返回的文本合成音频（result.mp3）
        recognize = threading.Thread(target=audio_recognize, args=('output.wav',))
        recognize.start()
        recognize.join()

        # 播放合成后的机器人文件
        play = threading.Thread(target=play_mp3, args=('result.mp3',))
        play.start()
        play.join()
