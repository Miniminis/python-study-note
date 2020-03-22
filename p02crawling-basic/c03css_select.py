# lxml 사용 기초 스크래핑
# 네이버 뉴스 가져오기
# pip install lxml, requests, cssselect
# lib import

import requests
import lxml.html


def main():
    response = requests.get("https://www.naver.com/")
    urls = scrape_news_list(response)

    for url in urls:
        print('url : {}'.format(url))


def scrape_news_list(response):
    urls = []

    root = lxml.html.fromstring(response.content)
    print('root : {}'.format(root)) # 결과 : root : <Element html at 0x3109b0>
    # print('response.content : {}'.format(response.content)) # 결과 : html 문서 전체 

    for a in root.cssselect('.api_list .api_item a.api_link'):
        url = a.get('href')
        urls.append(url)
    return urls


if __name__ == "__main__":
    main()
