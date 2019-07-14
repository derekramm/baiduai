from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '16774467'
API_KEY = 'WG5v9QzXqcmlcTQA8kpL7Ean'
SECRET_KEY = 'eKwAIGkK0pgsKVr88Fydh0tfjmgVRpFE'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result = client.synthesis('你也好啊', 'zh', 1, {
    'vol': 5, 'per': 4, 'spd': 2
})

if not isinstance(result, dict):
    with open('result.mp3', 'wb') as f:
        f.write(result)
