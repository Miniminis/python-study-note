# Request 
# http://httpbin.org/

import requests

session = requests.Session()
rep = session.get('https://www.naver.com/')
# print(rep.text)
# print(rep.ok)
# print(rep.status_code)
session.close()

# Cookei Return
s = requests.Session()
rep = s.get('http://httpbin.org/cookies', cookies={'name': 'niceman'})
# print(rep.text)
"""
{
  "cookies": {
    "name": "niceman"
  }
}
"""

# Cookie Set 
rep = s.get('http://httpbin.org/cookies/set', cookies={'name': 'niceman'})
# print(rep.text)


# User-Agent 
url = "https://www.daum.net/"
headers = {
    'User-Agent': 'chrome'
}

reps = s.get(url, headers=headers)
# print(reps.text)

s.close()   # session 비활성화 

with requests.Session() as sess:
    rep = sess.get('http://www.naver.com')
    print(rep.text)








