# https://wikidocs.net/7014

# 화면에 Hello World 문자열을 출력하세요.
print('Hello World')

# 화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)
print("Mary's cosmetics")

# 화면에 아래 문장을 출력하세요. (중간에 "가 있음에 주의하세요.)
# 신씨가 소리질렀다. "도둑이야".
print('신씨가 소리질렀다. "도둑이야".')

# 화면에 "C:\Windows"를 출력하세요.
print(r"C:\Windows")

# 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.
print("안녕하세요.\n만나서\t\t반갑습니다.")

# print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.
print ("오늘은", "일요일")
print("오늘은월요일")
print("오늘은 일요일")

# print() 함수를 사용하여 다음과 같이 출력하세요.
# naver;kakao;sk;samsung
print("naver", "kakao", "sk", "samsung", sep=";")

# print() 함수를 사용하여 다음과 같이 출력하세요.
# naver/kakao/sk/samsung
print('naver', 'kakao', 'sk', 'samsung', sep="/")

# 다음 코드를 수정하여 줄바꿈이 없이 출력하세요. 
# (힌트: end='') print 함수는 두 번 사용합니다. 
# 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
# print("first");print("second")
print("first", end='');print("second")

# 5/3의 결과를 화면에 출력하세요.
print(5/3)

# 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
samsung = 50000
cnt = 10
tot = samsung * cnt
print(tot)

# 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

# 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
s = "hello"
t = "python"
# 두 변수를 이용하여 아래와 같이 출력해보세요.
# 실행 예:
# hello! python
print('{}! {}'.format(s, t))

# 아래 코드의 실행 결과를 예상해보세요.
# >> 2 + 2 * 3 
print(2 + 2 * 3)

# 아래 변수에 바인딩된 값의 타입을 판별해보세요.
a = "132"
print(a, type(a))
# str

# 문자열 '720'를 정수형으로 변환해보세요.
num_str = "720"
print(int(num_str), type(int(num_str)))

# 정수 100을 문자열 '100'으로 변환해보세요.
num = 100
print(str(num), type(str(num)))

# 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
print(float("15.79"), type(float("15.79")))

# year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
year = "2020"
int_year = int(year) 
print(int_year, type(int_year))
print(int_year, int_year-1, int_year-2)

# 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
per_mon = 48584
tot_mon = 36
tot_money = per_mon * tot_mon
print(format(tot_money, ","))


# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letters = 'python'
# 실행 예
# p t
print(letters[0], letters[2])

# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "24가 2210"
# 실행 예: 2210
print(license_plate[-4:])

# 아래의 문자열에서 '홀' 만 출력하세요.
string = "홀짝홀짝홀짝"
# 실행 예:
# 홀홀홀
print(string[::2])  #시작인덱스:끝인덱스:오프셋

# 문자열을 거꾸로 뒤집어 출력하세요.
string = "PYTHON"
# 실행 예:
# NOHTYP
print(string[::-1])

# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
phone_number = "010-1111-2222"
# 실행 예
# 010 1111 2222
print(phone_number.replace("-", " "))

# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
# 실행 예
# 01011112222
print(phone_number.replace("-", ""))

# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
url = "http://sharebook.kr"
# 실행 예:
# kr
print(url[-2:])

# 아래 코드의 실행 결과를 예상해보세요.
# lang = 'python'
# lang[0] = 'P'
# print(lang)

# 'lang' does not support item assignmentpylint(unsupported-assignment-operation)
# Traceback (most recent call last):
#   File "C:\Users\minhe\Documents\github_miniminis\python-study-note\c01basic\sec04-6.py", line 138, in <module>
#     lang[0] = 'P'
# TypeError: 'str' object does not support item assignment



# 아래 코드의 실행 결과를 예상해보세요.
string = 'abcd'
string.replace('b', 'B')
print(string)
# 'abcd'


# 아래 코드의 실행 결과를 예상해보세요.
a = "3"
b = "4"
print(a + b)
print("34")

# 아래 코드의 실행 결과를 예상해보세요.
print("Hi" * 3)
print("HiHiHi")

# 화면에 '-'를 80개 출력하세요.
# 실행 예:
# --------------------------------------------------------------------------------
print('-'*80)


# 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
t1 = 'python'
t2 = 'java'
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.

# 실행 예:
# python java python java python java python java

print((t1 + " " + t2 + " ")*4)


# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13

print('이름: %s 나이: %d' %(name1, age1))
print('이름: %s 나이: %d' %(name2, age2))

# 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.
print('이름: {} 나이: {}'.format(name1, age1))
print('이름: {} 나이: {}'.format(name2, age2))

# 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.
# f-string은 문자열 앞에 f가 붙은 형태입니다. f-string을 사용하면 {변수}와 같은 형태로 문자열 사이에 타입과 상관없이 값을 출력할 수 있습니다.
print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')

# 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
상장주식수 = "5,969,782,550"
print(int(상장주식수.replace(',', '')), type(int(상장주식수.replace(',', ''))))

# 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
data = "   삼성전자    "
print(data.strip())

# 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
ticker = "btc_krw"
print(ticker.upper())

# 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
ticker = "BTC_KRW"
print(ticker.lower())

# 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
str = 'hello'
print(str.capitalize())

# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
file_name = "보고서.xlsx"
print(file_name.endswith('.xlsx'))

# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
file_name = "보고서.xls"
print(file_name.endswith(('xlsx', 'xls')))

# 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.
file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020'))

# 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
a = "hello world"
print(a.split(' '))


# 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
ticker = "btc_krw"
print(ticker.split('_'))

# 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
date = "2020-05-01"
print(date.split('-'))

# 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
data = "039490     "
print(data.rstrip())    # 공백이 제거된 새로운 string 이 생성된다. 기존의 string 은 자동으로 메모리에서 삭제됨 

# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
print(movie_rank)

# 051의 movie_rank 리스트에 "배트맨"을 추가하라.
movie_rank.append('배트맨')
movie_rank.insert(3, '배트맨')
print(movie_rank)

# movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, '슈퍼맨')
print(movie_rank)

# movie_rank 리스트에서 '럭키'를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
movie_rank.remove('럭키')
print(movie_rank)

# movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

# lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
# 실행 예:
# >> langs
# ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']

langs = lang1 + lang2
print(langs)


# 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
nums = [1, 2, 3, 4, 5, 6, 7]
print(min(nums))
print(max(nums))

# 다음 리스트의 합을 출력하라.
nums = [1, 2, 3, 4, 5]
print(sum(nums))

# 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 다음 리스트의 평균을 출력하라.
nums = [1, 2, 3, 4, 5]
sum = sum(nums)
len = len(nums)
print(sum / len)

# price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
price = ['20180728', 100, 130, 140, 150, 160, 170]
# 출력 예시:
# [100, 130, 140, 150, 160, 170]
print(price[1:])

# 슬라이싱을 사용해서 홀수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# [1, 3, 5, 7, 9]
print(nums[::2])

# 슬라이싱을 사용해서 짝수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# [2, 4, 6, 8, 10]
print(nums[1::2])

# 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
nums = [1, 2, 3, 4, 5]
# 실행 예:
# [5, 4, 3, 2, 1]
# nums.sort(reverse=True)
nums.reverse()
print(nums)

# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 Naver
print(interest[0] + " " + interest[2])





# interest 리스트에는 아래의 데이터가 바인딩되어 있다.

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
print(" ".join(interest))

# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.

# 출력 예시:
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우

print("/".join(interest))




# interest 리스트에는 아래의 데이터가 바인딩되어 있다.

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.

# 출력 예시:
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우
print('\n'.join(interest))





# 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.

string = "삼성전자/LG전자/Naver"
# 이를 interest 이름의 리스트로 분리 저장하라.

# 실행 예시
# >> print(interest)
# ['삼성전자', 'LG전자', 'Naver']
print(string.split('/'))


# 리스트에 있는 값을 오름차순으로 정렬하세요.
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)


# my_variable 이름의 비어있는 튜플을 만들라.
my_variable = ()
print(type(my_variable))



# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)
# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키

movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
print(movie_rank)


# 숫자 1 이 저장된 튜플을 생성하라.
tuple_one = (1, )
print(tuple_one)



# 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
t = (1, 2, 3)
# t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
# 튜플은 요소를 수정하거나 삭제할 수 없음 



# 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
t = 1, 2, 3, 4  # 튜플은 괄호가 없어도 튜플로서 인식된다!


# 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
t = ('a', 'b', 'c')
list_t = list(t)
list_t.remove('a')
list_t.insert(0, 'A')
print(tuple(list_t))



# 다음 튜플을 리스트로 변환하라.
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(list(interest))


# 다음 리스트를 튜플로 변경하라.
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(tuple(interest))


# 다음 코드의 실행 결과를 예상하라.
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
# 'apple', 'banana', 'cake'
# apple banana cake


# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
# (2, 4, 6, 8 ... 98)
print(tuple(range(2, 100, 2)))


# 기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다. 
# 하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있습니다. 
# 튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없습니다.
# >> a, b, *c = (0, 1, 2, 3, 4, 5)
# >> a
# 0
# >> b
# 1
# >> c
# [2, 3, 4]
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores
print(valid_score)



# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, _, *valid_score = scores
print(valid_score)


# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, *valid_score, _ = scores
print(valid_score)


# temp 이름의 비어있는 딕셔너리를 만들라.
temp = {}
print(type(temp))


# 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.
# 이름	희망 가격
# 메로나	1000
# 폴라포	1200
# 빵빠레	1800
snack_dict = {'메로나' : 1000, '폴라포' : 1200, '빵빠레' : 1800}
print(snack_dict)



# 085 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
# 이름	희망 가격
# 죠스바	1200
# 월드콘	1500
snack_dict['죠스바'] = 1200
snack_dict['월드콘'] = 1500
print(snack_dict)



# 다음 딕셔너리를 사용하여 메로나 가격을 출력하라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
# 실행 예:
# 메로나 가격: 1000

print('메로나 가격 : ', ice['메로나'])




# 다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
ice['메로나'] = 1300
print(ice)



# 다음 딕셔너리에서 메로나를 삭제하라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

del ice['메로나']
print(ice)



# 다음 코드에서 에러가 발생한 원인을 설명하라.

# >> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# >> icecream['누가바']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['누가바']
# KeyError: '누가바'
# key 값이 존재하지 않아서.





# 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라. 딕셔너리의 이름은 inventory로 한다.
# 이름	가격	재고
# 메로나	300	20
# 비비빅	400	3
# 죠스바	250	100
inventory = {'메로나' : [300, 20], '비비빅' : [400,	3], '죠스바' : [250, 100] }
print(inventory)



# inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
# 실행 예시:
# 300 원

print(inventory['메로나'][0])




# inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
# 실행 예시:
# 20 개
print(inventory['메로나'][1])



# inventory 딕셔너리에 아래 데이터를 추가하라.

inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
# 이름	가격	재고
# 월드콘	500	7
# 실행 예시:
# >> print(inventory)
# {'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100], '월드콘': [500, 7]}

inventory['월드콘'] = [500, 7]
print(inventory)



# 다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(list(icecream.keys()))


# 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(list(icecream.values()))



# icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# 출력 예시:
# 6700
# print(sum(icecream.values()))





# 098 딕셔너리 update 메서드
# 아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가하라.

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
# 실행 예시:
# >> print(icecream)
# {'탱크보이': 1200,  '폴라포': 1200,  '빵빠레': 1800,  '월드콘': 1500,  '메로나': 1000,  '콜라': 700,  '사이다': 700}
icecream.update(new_product)
print(icecream)





# 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
# 실행 예시:
# >> print(result)
# {'apple': 300, 'pear': 250, 'peach': 400}

print(dict(zip(keys, vals)))




# date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
# 실행 예시:
# >> print(close_table)
# {'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}
print(dict(zip(date, close_price)))