'''
pip install requests, beautifulsoup4, lxml(htmlparser)
'''

import requests
from bs4 import BeautifulSoup
import time
import json

KAKAO_TOKEN = "BIqPo5mWbc2RA3BKQdnjgNyq7uWKTWyGTpexMwopcJ8AAAFv_-KOpA"

def sendMsg(text):
    header = {"Authorization": 'Bearer' + KAKAO_TOKEN}
    url = "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
    post = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
        "button_title": "바로 확인"
    }

    data = {"template_object", json.dumps(post)}
    return requests.post(url, headers=header, data=data)

def rateAlert(condition):
    appId = condition["appId"]
    url = "https://play.google.com/store/apps/details?id={}&hl=ko".format(appId)

    r = requests.get(url)
    # print(r)
    # print(r.content)
    # print(r.text)       
    # print(type(r.content))  #<class 'bytes'>
    # print(type(r.text))     #<class 'str'>

    bs = BeautifulSoup(r.content, "lxml")
    # print(bs.find_all('a')[0])
    rateSec = bs.select("span.EymY4b")[0]     # select의 결과는 리스트!
    rate = int(rateSec.select("span")[1].text.replace(",", ""))
    print("현재 총 리뷰 수: {} : {}".format(rate, time.strftime('%c', time.localtime(time.time()))))
    
    if rate == rate+1:
        rate = rate+1
        text = "새로운 리뷰가 등록되었습니다. 현재까지의 총 리뷰 수: {}, 등록시간: {}".format(rate, time.strftime('%c', time.localtime(time.time())))
        print(text)     
        # print(sendMsg(text).text)
        
if __name__ == "__main__":
    condition = {
        "appId": "kr.co.quicket"
    }
    while True:
        rateAlert(condition)
        time.sleep(5)
