# encar 중고차 사이트 정보 GET 데이터 통신 

from urllib.request import urlopen
from urllib.parse import urlparse, urlencode

BASE_URL = "http://www.encar.com/index.do"

mem = urlopen(BASE_URL)

# GET 통신 결과 확인
print('type : {}'.format(type(mem)))
print("status : {}".format(mem.status))
print("url : {}".format(mem.url))
print("headers : \n{}".format(mem.headers))
print("code : {}".format(mem.code))
print("read : {}".format(mem.read(100).decode('utf-8')))
print("parse : {}".format(urlparse('http://www.encar.com/index.do?id=mini&pw=1111')))
print("parse : {}".format(urlparse('http://www.encar.com/index.do?id=mini&pw=1111').query))


print("==============================================================================")

BASE_URL_2 = "https://api.ipify.org"

values = {
    'format' : 'json'
    # 'format' : 'text'
    # 'format' : 'jsonp'
}

print('before param : {}'.format(values))
params = urlencode(values)      # url parameter 형식으로 encoding 해주는 function
print('after param : {}'.format(params))

URL = BASE_URL_2 + "?"+ params
print('요청 URL : {}'.format(URL))

data = urlopen(URL).read()
text = data.decode('utf-8')
print('data : {}'.format(data))
print('text : {}'.format(text))

# 결과 
# data : b'{"ip":"59.5.242.183"}'
# text : {"ip":"59.5.242.183"}

# data : b'59.5.242.183'
# text : 59.5.242.183

# data : b'callback({"ip":"59.5.242.183"});'
# text : callback({"ip":"59.5.242.183"});
