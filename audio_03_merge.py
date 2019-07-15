from aip import AipSpeech

APP_ID = '16774467'
API_KEY = 'WG5v9QzXqcmlcTQA8kpL7Ean'
SECRET_KEY = 'eKwAIGkK0pgsKVr88Fydh0tfjmgVRpFE'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def audio_merge(message, wave_output_path='result.mp3'):
    """
    语音合成
    :param message:  # 要合成语音的文本
    :param wave_output_path: # 输出的音频文件路径
    :return:
    """
    result = client.synthesis(message, 'zh', 1, {
        'vol': 5, 'per': 4, 'spd': 2
    })

    # 输出到音频
    if not isinstance(result, dict):
        with open(wave_output_path, 'wb') as f:
            f.write(result)
