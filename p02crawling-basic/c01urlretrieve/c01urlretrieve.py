# 크롤링 기초 

# 1. import lib
# 2. url 설정 
# 3. 다운받을 경로 설정 
# 4. 예외처리

import urllib.request as req

img_url = "https://images.theconversation.com/files/307636/original/file-20191218-11891-rdedzs.jpg?ixlib=rb-1.1.0&rect=0%2C601%2C4611%2C2965&q=45&auto=format&w=926&fit=clip"
html_url= "https://www.google.com"

save_path1 = "C:/Users/CrePASS/Documents/GitHub/python-study-note/p02crawling-basic/sample_image.jpg"      
save_path2 = "C:/Users/CrePASS/Documents/GitHub/python-study-note/p02crawling-basic/index.html"

# save_path1 = "C:/python-crawling/"      # 파일 이름, 포맷 명시 안하면 permission denied 에러 뜸 
# save_path2 = "C:/python-crawling/index.html"

try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('Download 실패')
    print(e)
else :
    # header 정보 출력해보기
    print(header1)
    print(header2)

    # file 형식 출력
    print('Filename 1 : {}'.format(file1))
    print('Filename 2 : {}'.format(file2))

    # 전송성공!
    print('Download Success!!!')



# 결과
# Connection: close
# Content-Length: 55246
# Last-Modified: Mon, 24 Feb 2020 10:31:16 GMT
# Cache-Control: public, max-age=31536000
# Server: imgix
# X-Imgix-ID: 6c89ed49152677665f2385f57357550a2a41b3d8
# Date: Mon, 02 Mar 2020 23:53:17 GMT
# Age: 652936
# Accept-Ranges: bytes
# Content-Type: image/jpeg
# Access-Control-Allow-Origin: *
# X-Content-Type-Options: nosniff
# X-Served-By: cache-lax8636-LAX, cache-bur17578-BUR
# X-Cache: HIT, HIT
# Vary: Accept, User-Agent


# Date: Mon, 02 Mar 2020 23:53:17 GMT
# Expires: -1
# Cache-Control: private, max-age=0
# Content-Type: text/html; charset=ISO-8859-1
# P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
# Server: gws
# X-XSS-Protection: 0
# X-Frame-Options: SAMEORIGIN
# Set-Cookie: 1P_JAR=2020-03-02-23; expires=Wed, 01-Apr-2020 23:53:17 GMT; path=/; domain=.google.com; Secure
# Set-Cookie: NID=199=h1Kz0zQtG4dLG9tlPoHgMBmnllcpmkT5-JhYS0cZhzhxV9-7jd64iDBoFlv5L1Pe1nJ9Da2Tvx2PYyA20C5NusnLg79aG6bYnDPkULWJ9oZRn_3Yl7u_4fnLgacga9Qx-sZtte8CIYVOGhboNvkJAcVvnNJNe5azmf7DJHpkUx0; expires=Tue, 01-Sep-2020 23:53:17 GMT; path=/; domain=.google.com; HttpOnly
# Alt-Svc: quic=":443"; ma=2592000; v="46,43",h3-Q050=":443"; ma=2592000,h3-Q049=":443"; ma=2592000,h3-Q048=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000
# Accept-Ranges: none
# Vary: Accept-Encoding

# Filename 1 : C:/python-crawling/image02.jpg
# Filename 2 : C:/python-crawling/index.html
# Download Success!!
    

