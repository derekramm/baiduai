from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '16774467'
API_KEY = 'WG5v9QzXqcmlcTQA8kpL7Ean'
SECRET_KEY = 'eKwAIGkK0pgsKVr88Fydh0tfjmgVRpFE'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()

# 识别本地文件
result = client.asr(get_file_content('output.wav'), 'wav', 16000, {
    'dev_pid': 1536,  # 普通话(支持简单的英文识别)
})

print(result)