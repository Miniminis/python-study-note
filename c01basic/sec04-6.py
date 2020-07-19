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