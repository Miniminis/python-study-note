# 행정안전부 RSS 피드 읽어오기 

from urllib.request import urlopen
from urllib.parse import urlparse, urlencode

URL = 'https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp'
params = []

for p in [1001, 1013, 1014]:
    params.append(dict(ctxCd=p))

for param in params:
    encodeParam = urlencode(param)
    New_URL = URL + "?"+encodeParam
    contents = urlopen(New_URL).read().decode('utf-8')
    print(contents)
    print("=" * 50)


## 정리 
# 기본 url 
# param 만들어주기 dict(ctxCd=p)
# urlencode 로 url parameter 형식으로 만들어주기 
# 기본 url + ? + 만들어진 url = 새로운 url 
# 새 url 로 open, read, decode 해서 contents 값 받아오기 
# 출력 