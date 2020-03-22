# 1. 라이브러리 설치 
# 2. 다운 받을 path 및 filename 
# 3. url 설정 
# 4. 예외처리 

import urllib.request as req
from urllib.error import HTTPError, URLError

path_list = ["C:/Users/minhe/Documents/GitHub/python-study-note/p02crawling-basic/c02urlopen/c02urlopenImg.jpg", 
                "C:/Users/minhe/Documents/GitHub/python-study-note/p02crawling-basic/c02urlopen/c02urlopenIndex.html"]

target_url = ["https://t1.daumcdn.net/liveboard/petnu/9ba55cc775504cb0bdf4c37d4e885ceb.JPG", 
                "https://www.google.com/"]

for i, url in enumerate(target_url):
    try:
        # 웹 수신 정보 읽기 
        # urlopen() 은 정보를 읽기만 하고 다운로드는 안함. 
        # urlretrieve 는 정보 읽고 다운 같이! 
        response = req.urlopen(url)

        # 수신 내용 
        content = response.read()
        print("---------------------------")

        # 상태정보 중간 출력 
        print("Header Info - {} : {}".format(i, response.info()))
        print("HTTP status code : - {}".format(response.getcode()))
        print("---------------------------")

        # 가져온 데이터 파일로 적기 (write)
        with open(path_list[i], 'wb') as c:
            c.write(content)

    except HTTPError as e:
        print("Download failed")
        print("HTTPError Code: ", e.code)
    except URLError as e:
        print("Download failed")
        print("URL ERROR Reason : ", e.reason)
    else:   
        print()
        print("Download Succeed")


# ---------------------------
# Header Info - 0 : Date: Mon, 16 Mar 2020 23:59:20 GMT
# Server: PWS/8.3.2.7
# X-Px: ms h0-s1388.p46-icn ( h0-s1398.p46-icn), rf-ht h0-s1398.p46-icn ( h0-s767.p61-icn), ht h0-s767.p61-icn.cdngp.net
# Age: 4100
# Cache-Control: max-age=21600
# Expires: Tue, 17 Mar 2020 04:51:00 GMT
# Accept-Ranges: bytes
# Content-Length: 226941
# Content-Type: image/jpeg
# Last-Modified: Mon, 26 Mar 2018 06:59:25 GMT
# Connection: close


# HTTP status code : - 200
# ---------------------------

# Download Succeed

# ---------------------------
# Header Info - 1 : Date: Mon, 16 Mar 2020 23:59:21 GMT
# Expires: -1
# Cache-Control: private, max-age=0
# Content-Type: text/html; charset=ISO-8859-1
# P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
# Server: gws
# X-XSS-Protection: 0
# X-Frame-Options: SAMEORIGIN
# Set-Cookie: 1P_JAR=2020-03-16-23; expires=Wed, 15-Apr-2020 23:59:21 GMT; path=/; domain=.google.com; Secure
# Set-Cookie: NID=200=EI-Kxj7OsWjVBQr5eMtVDI3Wet6aI4AFjHL7-VtLGBZ2PPGXERsmlpmxoM0sUhcJsSw7TBcNpytov0MWwhp9KPEQ1XJ9djSgdWl7QtVHTvNNT0edIO-1hHYAW3kX9g9W4BYCRGPA6D2cBXjqDAC8dAvMF9Lr6ycrI4WapSUyN5o; expires=Tue, 15-Sep-2020 23:59:21 GMT; path=/; domain=.google.com; HttpOnlyMT; path=/; domain=.google.com; HttpOnly
# Alt-Svc: quic=":443"; ma=2592000; v="46,43",h3-Q050=":443"; ma=2592000,h3-Q049=":443"; ma=2592000,h3-Q048=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000
# Accept-Ranges: none
# Vary: Accept-Encoding
# Connection: close


# HTTP status code : - 200
# ---------------------------

# Download Succeed