from aip import AipSpeech
from tulint_robot import chat
from audio_03_merge import audio_merge

APP_ID = '16774467'
API_KEY = 'WG5v9QzXqcmlcTQA8kpL7Ean'
SECRET_KEY = 'eKwAIGkK0pgsKVr88Fydh0tfjmgVRpFE'

# 创建百度AI平台请求的客户端对象
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取音频文件，返回二进制字节流
def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()

def audio_recognize(file_path='output.wav'):
    """
    语音识别：语音转文字
    :return:
    """

    # 识别本地文件
    result = client.asr(
        get_file_content(file_path),  # 上传给百度的音频文件二进制字节流
        'wav',  # 上传音频的格式
        16000,  # 音频码率
        {
            'dev_pid': 1536,  # 普通话(支持简单的英文识别)
        }
    )

    """返回结果示例（字典类型）
    d = {
        'corpus_no': '6713864969214803328',
        'err_msg': 'success.',
        'err_no': 0,
        'result': ['开始录制'],
        'sn': '902955053681563193502'
    }
    """

    print('我：', result['result'][0])  # 输出识别出来的文本

    robot_reply = chat(result['result'][0])[1]  # 获取图灵机器人的响应
    audio_merge(robot_reply, 'result.mp3')  # 合成音频
    print(robot_reply)  # 输出图灵机器人的响应文本

if __name__ == '__main__':
    audio_recognize()
