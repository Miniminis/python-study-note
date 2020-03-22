import os
import urllib.parse as parse
import urllib.request as req

from bs4 import BeautifulSoup

from fake_useragent import UserAgent

opener = req.build_opener()
opener.addheaders = [('User-Agent', UserAgent().chrome)]
req.install_opener(opener)

BASE_URL = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
keyword = parse.quote_plus("보노보노")
URL = BASE_URL + keyword

rep = req.urlopen(URL)

savePath = "C:/Users/minhe/Documents/GitHub/python-study-note/p02crawling-basic/c10BeautifulSoup02ImgFolder/"

try:
    if not (os.path.isdir(savePath)):
        os.mkdir(os.path.join(savePath))
except OSError as e:
    print("Cannot Find Such Directory ERROR!")
    print("ERROR MSG : {}".format(e.filename))
else:
    print("Directory Successfully Created!!!")


soup = BeautifulSoup(rep, 'html.parser')
imgSrcList = soup.select('div.img_area > a.thumb > img')
for i, imgSrc in enumerate(imgSrcList, 1):
    fileName = os.path.join(savePath, savePath + str(i) + ".png")
    req.urlretrieve(imgSrc['data-source'], fileName)

# imgSrcList = soup.find_all('a', class_="thumb _thumb")
# for i, imgSrc in enumerate(imgSrcList, 1):
#     img_t = imgSrc.find('img')
#     fileName = os.path.join(savePath, savePath + str(i) + ".png")
#     req.urlretrieve(img_t.attrs['data-source'], fileName)

print('DOWNLOAD SUCCEED!')

