import json
import urllib.request

api_url = "http://openapi.tuling123.com/openapi/api/v2"


def chat(text_input, image_url=None, media_url=None, req_type=0):
    req = {
        "reqType": req_type,  # 输入类型：0-文本(默认)、1-图片、2-音频
        "perception":  # 输入信息
            {
                "inputText":  # 文本信息
                    {
                        "text": text_input
                    },
                "inputImage": {  # 图片信息
                    "url": image_url
                },
                "inputMedia": {  # 音频信息
                    "url": media_url
                },
                "selfInfo": {  # 客户端属性
                    "location": {  # 地理位置信息
                        "city": "海淀区",
                        "province": "北京市",
                        "street": "北三环西路甲3号"
                    }
                }
            },
        "userInfo":  # 用户参数
            {
                "apiKey": "eac72b03fb4e4bc789d8ba8067c94f33",  # 机器人标识
                "userId": "342059"  # 用户唯一标识
            }
    }

    req = json.dumps(req).encode('utf-8')

    http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf-8')
    response_dic = json.loads(response_str)

    intent_code = response_dic['intent']['code']
    results_text = response_dic['results'][0]['values']['text']

    return str(intent_code), results_text


if __name__ == '__main__':
    while True:
        inp = input('我：')
        if inp == 'exit':
            break
        print('机器人', chat(inp)[1])
