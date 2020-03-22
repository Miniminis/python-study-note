"""
BeautifulSoup4 
* beautifulsoup4 4.8.2
* find, find_all, select, select_one 
"""

from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
    <h1>this is h1 area</h1>
    <h2>this is h2 area</h2>
    <p class="title">
        <b>The Dormouse's story</b>
    </p>
    <p class="story">Once upon a time there were three little sisters
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
        <a data-io="link3" href="http://example.com/tillie" class="brother" id="link3">Tillie</a>
    </p>
    <p class="story">
        story...
    </p>
</body>
</html>
"""

# 초기화 
soup = BeautifulSoup(html, 'html.parser')

# 타입 확인
print(type(soup))           # <class 'bs4.BeautifulSoup'>

# 코드 정리 
print(soup.prettify())        # html 문서 예쁘게 출력됨 

# h1 태그에 접근 
print(soup.html.body.h1)

# h1 태그 내부의 text 만 가져오기 
print(soup.html.body.h1.string)

# 쓸 수 있는 function check 
print(dir(soup))
"""
['ASCII_SPACES', 'DEFAULT_BUILDER_FEATURES', 'NO_PARSER_SPECIFIED_WARNING', 'ROOT_TAG_NAME', '__bool__', '__call__', '__class__', '__contains__', '__copy__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__unicode__', '__weakref__', '_all_strings', '_check_markup_is_url', '_feed', '_find_all', '_find_one', '_is_xml', '_lastRecursiveChild', '_last_descendant', '_linkage_fixer', '_most_recent_element', '_namespaces', '_popToTag', '_should_pretty_print', 'append', 'attrs', 'builder', 'can_be_empty_element', 'cdata_list_attributes', 'childGenerator', 'children', 'clear', 'contains_replacement_characters', 'contents', 'currentTag', 'current_data', 'declared_html_encoding', 'decode', 'decode_contents', 'decompose', 'descendants', 'element_classes', 'encode', 'encode_contents', 'endData', 'extend', 'extract', 'fetchNextSiblings', 'fetchParents', 'fetchPrevious', 'fetchPreviousSiblings', 'find', 'findAll', 'findAllNext', 'findAllPrevious', 'findChild', 'findChildren', 'findNext', 'findNextSibling', 'findNextSiblings', 'findParent', 'findParents', 'findPrevious', 'findPreviousSibling', 'findPreviousSiblings', 'find_all', 'find_all_next', 'find_all_previous', 'find_next', 'find_next_sibling', 'find_next_siblings', 'find_parent', 'find_parents', 'find_previous', 'find_previous_sibling', 'find_previous_siblings', 'format_string', 'formatter_for_name', 'get', 'getText', 'get_attribute_list', 'get_text', 'handle_data', 'handle_endtag', 'handle_starttag', 'has_attr', 'has_key', 'hidden', 'index', 'insert', 'insert_after', 'insert_before', 'isSelfClosing', 'is_empty_element', 'is_xml', 'known_xml', 'markup', 'name', 'namespace', 'new_string', 'new_tag', 'next', 'nextGenerator', 'nextSibling', 'nextSiblingGenerator', 'next_element', 'next_elements', 'next_sibling', 'next_siblings', 'object_was_parsed', 'original_encoding', 'parent', 'parentGenerator', 'parents', 'parse_only', 'parserClass', 'parser_class', 'popTag', 'prefix', 'preserve_whitespace_tag_stack', 'preserve_whitespace_tags', 'prettify', 'previous', 'previousGenerator', 'previousSibling', 'previousSiblingGenerator', 'previous_element', 'previous_elements', 'previous_sibling', 'previous_siblings', 'pushTag', 'recursiveChildGenerator', 'renderContents', 'replaceWith', 'replaceWithChildren', 'replace_with', 'replace_with_children', 'reset', 'select', 'select_one', 'setup', 'smooth', 'string', 'strings', 'stripped_strings', 'tagStack',
'text', 'unwrap', 'wrap']
"""

# list 출력 
p2 = soup.html.body.p.next_sibling.next_sibling
print(list(p2.next_elements))

for elem in p2.next_elements:
    print("="*50)
    print(elem)
# 결과 : p2 이후의 모든 elements 들이 출력됨, p, a, string 각각 


# p tag 접근 
print(soup.html.body.p)
print(soup.html.body.p.next_sibling.next_sibling)




## soup 초기화 
soup = BeautifulSoup(html, "html.parser")

# find_all
aList = soup.find_all('a')
print(type(aList))      # <class 'bs4.element.ResultSet'>
print(aList)

# find_all with class 
aList = soup.find_all("a", class_="sister")     # id="link2" , string="Tillie" , string=["Elsie","Tillie"] , {} 다중 조건
aList02 = soup.find_all("a", id="link2")
aList03 = soup.find_all("a", string="Tillie")
aList04 = soup.find_all("a", string=["Elsie","Tillie"])
print(aList04)

# find
firstA = soup.find('a')
print(firstA)
print(firstA.string)
print(firstA.text)

# 다중조건 적용 
multiConditionedA = soup.find('a', {"class" : "sister", "id":"link1"})
print(multiConditionedA)
print(multiConditionedA.string)
print(multiConditionedA.text)




# select, select_one 
# CSS 선택자로 접근할 때 : select, select_one
# tag 로 접근할 때 : find, find_all

selectedA = soup.select('a')        # list 
print(selectedA) 

selectedOneA = soup.select_one('p.title > b')
selectedOneA02 = soup.select_one('a#link2')
print(selectedOneA)
print(selectedOneA02)

link3 = soup.select_one("a[data-io='link3']")       # .class / #id / tag[custom-attr=""]
print(link3)


# 선택자에 맞는 전체 선택
# 태그 + 클래스 + 자식      
# return list
link4 = soup.select("p.story > a")
# 태그 + 클래스 + 자식 + 태그 + 순서
link5 = soup.select("p.story > a:nth-of-type(2)")
# 태그 + 클래스
link6 = soup.select("p.story")

# 전체 구조 및 텍스트 출력
print(link4)
print(link5)
print(link6[1])