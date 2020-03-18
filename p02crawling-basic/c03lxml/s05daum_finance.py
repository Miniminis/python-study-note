"""
다음 주식정보 가져오기 
1. fake-UserAgent 사용  
2. header 에 정보 삽입하여 get 요청
3. 수신 데이터 가공 및 추출 
"""

"""
1. 가짜 유저 agent 생성 
2. header 생성 
3. header 와 함께 get 요청하기
4. 받아온 정보 가공하기 
"""

import json
import urllib.request as req
from fake_useragent import UserAgent

ua = UserAgent()
# print(ua.msie)
# print(ua.ie)
# print(ua.safari)
# print(ua.chrome)
# print(ua.firefox)
# print(ua.random)

header = {
    'User-Agent' : ua.chrome,
    'Referer' : 'http://finance.daum.net/'
}

URL = "http://finance.daum.net/api/search/ranks?limit=10"

content = req.urlopen(req.Request(URL, headers=header)).read().decode('utf-8')
rank_json = json.loads(content)['data']

for elm in rank_json:
    print('rank : {} / name: {} / print: {} '.format(elm['rank'], elm.get('name'), elm['tradePrice']))


"""
결과 : 
rank : 1 / name: 삼성전자 / print: 45600
rank : 2 / name: SK하이닉스 / print: 73100
rank : 3 / name: 진원생명과학 / print: 7550
rank : 4 / name: 현대차 / print: 73500
rank : 5 / name: 셀트리온 / print: 157000
rank : 6 / name: 씨젠 / print: 59200.0
rank : 7 / name: 한국전력 / print: 17100
rank : 8 / name: 좋은사람들 / print: 2665
rank : 9 / name: 삼성전자우 / print: 38000
rank : 10 / name: LG화학 / print: 280000
"""