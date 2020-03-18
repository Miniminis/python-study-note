# lxml 기초02
# 네이버 뉴스 : 스크래핑02
# session, xpath 사용하기 

import requests
from lxml.html import fromstring, tostring


def main():
    session = requests.Session()    # session 사용 - 쿠키, 세션 등을 활용할 수 있음 

    response = requests.get("https://www.naver.com/")
    urls = scrape_news_list(response)
    # print(urls)

    for name, url in urls.items():
        print(name, url)


def scrape_news_list(response):
    urls = {}

    root = fromstring(response.content)
    # print('root : {}'.format(root)) # 결과 : root : <Element html at 0x3109b0>
    # print('response.content : {}'.format(response.content)) # 결과 : html 문서 전체 

    for a in root.xpath('//ul[@class="api_list"]/li[@class="api_item"]/a[@class="api_link"]'):
        # print(a)
        # print(tostring(a, pretty_print=True))
        name, url = extract_content(a)
        urls[name] = url
    return urls


def extract_content(a):
    link = a.get("href")
    name = a.xpath('./img')[0].get('alt')
    # print(name)
    # 결과 : [<Element img at 0x337f320>]
        # [<Element img at 0x337f320>]
        # [<Element img at 0x337f320>]
        # [<Element img at 0x337f320>]
        # [<Element img at 0x337f320>]
        # [<Element img at 0x337f320>]
        # [<Element img at 0x337f320>]
        # [<Element img at 0x337f320>]
        # [<Element img at 0x337f320>]
        # [<Element img at 0x337f320>]
        # [<Element img at 0x337f320>]
        # [<Element img at 0x337f320>]
        # [<Element img at 0x337f320>]
        # [<Element img at 0x337f320>]
        # [<Element img at 0x337f320>]
        # [<Element img at 0x337f320>]
        # [<Element img at 0x337f320>]
        # [<Element img at 0x337f320>]
    return name, link


if __name__ == "__main__":
    main()

