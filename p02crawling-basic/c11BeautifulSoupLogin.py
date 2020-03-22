""" 
1. 로그인 시 필요한 정보 확인 
2. login info dictionary  
3. header dictionary 
4. session, post 요청 - 로그인 확인 
5. 로그인 후 접근하고 싶은 페이지 sesstion, get 요청
6. crawling 할 데이터 가져오기  
"""

import requests as req
from fake_useragent import UserAgent 
from bs4 import BeautifulSoup

login_info = {
    'url': 'http%3a%2f%2fwww.auction.co.kr%2f',
    'seller': '', 
    'seqno': '',
    'pageType': 'PW',
    'id': 'blackgoat473',
    'checkboxKIDBase': 'on',
    'password': 'password!1',
    'Image1': '',
    'nonMembName': '',
    'nonMembTelNumber': '',
    'payPassword': '',
    'screen_height': '864',
    'screen_width': '1536',
    'isIpay': '',
    'siteType': '', 
    'accessToken': '',
    # 'pageType': 'P'   
}

header_info = {
    'User-Agent': UserAgent().chrome,
    'Referer': 'https://memberssl.auction.co.kr/Authenticate/?url=http%3a%2f%2fwww.auction.co.kr%2f&return_value=0',
}

header_info_after_login = {
    'User-Agent': UserAgent().chrome,
    'Cookie': 'pcid=1584867073817; sguid=31584867074372004891280000; pguid=21584867074372004891010000; tbseg=203013; cguid=11561859337729001011000000; ASP.NET_SessionId=ahcdvj1h3imbilskfbzzwlbk; APAC=kid=4QIIDMVTZgVsrmQYB89dWXeFq0NkMA72&lgdt=200322&acdt=200322&tmcnt=1&lmcnt=0&lpdt1=200322&lpdt2=200321; auctionGrade=MBType=1&buyGradeType=0&BGT=8bWVT8WjdqudI%2bP%2fMpnkeRxMuEddhtplp%2frmqPknXM8%3d; auctioncommon=hmac=A9Znzf4z%2bo1z1GjvB1bIbuxxsFE%3d&segmentid=14&couponqty=0&MSNum=167391163; store=storeid=; sellplus=membcode=&usedate=; bcp=%uc190%ubbfc%ud76c|2|0|N|0; AGP=ws=&am=wBr5MmKfHQrX2fTtY0ZkcDabbCxxDUWTd&mst=IB1&bm=N&babyplus=N&petplus=N; uwtmp=fc%3d5%26fgc%3d5%26cnc%3d0%26cmc%3d0; captcha=LBD_CaptchaCodeCollection_postback=/wEy4wQAAQAAAP////8BAAAAAAAAAAwCAAAARkxhbmFwLkJvdERldGVjdCwgVmVyc2lvbj0yLjAuOS4yLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPW51bGwFAQAAACVMYW5hcC5Cb3REZXRlY3QuQ2FwdGNoYUNvZGVDb2xsZWN0aW9uAgAAAAtfY29sbGVjdGlvbghfdGltZW91dAMAHFN5c3RlbS5Db2xsZWN0aW9ucy5IYXNodGFibGUIAgAAAAkDAAAAsAQAAAQDAAAAHFN5c3RlbS5Db2xsZWN0aW9ucy5IYXNodGFibGUHAAAACkxvYWRGYWN0b3IHVmVyc2lvbghDb21wYXJlchBIYXNoQ29kZVByb3ZpZGVyCEhhc2hTaXplBEtleXMGVmFsdWVzAAADAwAFBQsIHFN5c3RlbS5Db2xsZWN0aW9ucy5JQ29tcGFyZXIkU3lzdGVtLkNvbGxlY3Rpb25zLklIYXNoQ29kZVByb3ZpZGVyCOxROD8BAAAACgoDAAAACQQAAAAJBQAAABAEAAAAAQAAAAYGAAAAIDkyMzQ0ZTc2Zjg3MTRmNzc4MzkyZTM4ZTU5MDA2MGU2EAUAAAABAAAACQcAAAAFBwAAABtMYW5hcC5Cb3REZXRlY3QuQ2FwdGNoYUNvZGUEAAAABV9jb2RlD19nZW5lcmF0aW9uVGltZRdfdXNlZEZvckltYWdlR2VuZXJhdGlvbhdfdXNlZEZvclNvdW5kR2VuZXJhdGlvbgEAAAANAQECAAAABggAAAAFTkVIVkOYFSxBj87XiAEAC1f3IBasADwBw/hTB4Uw4geUruBz; ssguid=3158486707437200489128000457; auction=wu1eMy8heYJQJVJbt0kwS6B1bgJT1O1wAG3ZnRcrH1CmbXXkWsqH0L0qluWXj%2fC6rXJP5wWF8UySV4y7p1Fl%2bX6cjuh1USCQdk0Gfkzfip5AL59DjerQ%2bmVh012bFMRpOLDY%2b7MRwS%2bUUcI45l1ZVRxuTdx9%2bYpr3l8CvAsIYp4BsGnndLfgBlq0OzWerOy%2f8'
}


with req.session() as s:
    rep = s.post('https://memberssl.auction.co.kr/Authenticate/?url=http%3a%2f%2fwww.auction.co.kr%2f%3fredirect%3d1&return_value=0', login_info, headers=header_info)

    if rep.status_code != 200:
        raise Exception('LOGIN FAILED!')
    
    # rep.content.decode('UTF-8')
    
    rep = s.get('http://favorite.auction.co.kr/BuyerTools/Favorites/FavoriteItemHome.aspx?Use_Yn=N', headers=header_info_after_login)
    # print(rep.text)
    
    soup = BeautifulSoup(rep.text, 'html.parser')
    isLoggedin = soup.find('div', class_="myauctionptitle")
    
    if isLoggedin is None:
        raise Exception('Login failed. Wrong Password.')

    rep = s.get('http://favorite.auction.co.kr/BuyerTools/Favorites/FavoritesItemList.aspx', headers=header_info_after_login)
    soup = BeautifulSoup(rep.text, 'html.parser')
    my_wish_list = soup.select('td.pname')

    for item in my_wish_list:
        item_no, item_name = item.select_one('div.lsmo').string.strip(), item.find('a').string.strip()
        item_num = item_no[1:11]
        # print(item_num)
        detail_url = "http://itempage3.auction.co.kr/DetailView.aspx?itemno={}&frm3=V2".format(item_num)
        print("no : {} & name: {} & link : {}".format(item_num, item_name, detail_url))
