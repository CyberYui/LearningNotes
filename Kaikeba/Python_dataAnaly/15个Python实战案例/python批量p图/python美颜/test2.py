import requests
import base64
import os
import random
import time
A_DIR = os.path.dirname(os.path.abspath(__file__))
path = A_DIR+'/未处理/'
paths = A_DIR+'/已处理/'
# key = 'j1eIBCbzSTcwoXFyHdrVn-3RURnwP3Nu'
# secret = 'w5RPm5a43r5DthilCgZiZFsBQxC0N8Si'
# key = 'DdEcM7-W4HbQ9Fm9kZx8CWUY7a92qEVy'
# secret = 'roQNqQnIFFssWhRF9WTpBg9-XIhmUOCX'
key = 'CUoUT966sE3mrPFg2D7bF26qF8pQNZEE'
secret = 'cwkj4DEOV_80a5mB9F_0O3FX99FHx95N'
#美白whitening  0-100
whitening = 100
#磨皮smoothing  0-100
smoothing = 100
#瘦脸thinface  0-100
thinface = 100
#小脸shrink_face 0-100
shrink_face = 100
#大眼enlarge_eye 0-100
enlarge_eye = 100
#眉毛remove_eyebrow 0-100
remove_eyebrow = 100
#滤镜filter_type
filter_type = 'beautify'
def find_face(imgpath):
    url = 'https://api-cn.faceplusplus.com/facepp/v2/beautify'
    data = {'api_key': key, 'api_secret': secret, 'image_url': imgpath, 'whitening': whitening,'smoothing':smoothing,
            'thinface':thinface,'shrink_face':shrink_face,'enlarge_eye':enlarge_eye,'remove_eyebrow':remove_eyebrow,
            'filter_type':filter_type}
    files = {'image_file': open(imgpath, 'rb')}
    response = requests.post(url, data=data, files=files)
    res_json = response.json()
    print(res_json)
    results = res_json['result']
    image = base64.b64decode(results)
    a = randomVerificationCode(5)
    with open(paths+a+'.jpg', 'wb') as file:
        file.write(image)
def randomVerificationCode(num):
    code = ''
    for i in range(num):
        code += chr(random.choice([random.randint(48,57),random.randint(65,90),random.randint(97,122)]))
    return code
if __name__ == '__main__':
    filename_list = os.listdir(path)
    for i in filename_list:
        time.sleep(2)#每两秒处理一张
        find_face(path+i)