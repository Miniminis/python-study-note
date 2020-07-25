# https://wikidocs.net/7028
# 조건문

# 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
print('boolean')

# 아래 코드의 출력 결과를 예상하라
print(3 == 5)   # false


# 아래 코드의 출력 결과를 예상하라
print(3 < 5)    # true

# 아래 코드의 결과를 예상하라.
x = 4
print(1 < x < 5)    # true

# 아래 코드의 결과를 예상하라.
print ((3 == 3) and (4 != 3))   # true


# 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.
# print(3 => 4)   # 지원하지않는 연산자

# 아래 코드의 출력 결과를 예상하라

if 4 < 3:
    print("Hello World")
# 아무것도 출력되지않음



# 아래 코드의 출력 결과를 예상하라

if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")
print('>>> Hi, there. ')


# 아래 코드의 출력 결과를 예상하라

if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
# 1, 2, 4

# 아래 코드의 출력 결과를 예상하라

if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
# 3, 5



# 사용자로부터 입력받은 문자열을 두 번 출력하라. 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과이다.
# >> 안녕하세요
# 안녕하세요안녕하세요

# user = input('인사해줘요.')
user = 'HELLO'
print(user * 2)



# 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.

# >> 숫자를 입력하세요: 30
# 40
# in_num = input('숫자 1개 입력 부탁쓰')
in_num = 12
print(int(in_num) + 10)


# 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.

# >> 30
# 짝수
num = 30
if(num % 2 == 0):
    print('짝수')
else:
    print('홀수')


# 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후
# 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를 아니면 
# "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.

warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

invest_product = "Microsoft"
if(invest_product in warn_investment_list):
    print('투자 경고 종목입니다')
else:
    print('투자 경고 종목이 아닙니다.')


# 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.
str = 'E'

print(''.join(str.upper() if str.islower() else str.lower()))

# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
num1 = 10
num2 = 32
num3 = 54

max = num1
if(num2 > num1):
    max = num2
if (num3 > num2):
    max = num3
print(max)


# 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
phnum_str = '01156984444'
phcom = phnum_str[0:3]
company = ''
if(phcom == '011'):
    com_type = 'SKT'
elif (phcom == '016'):
    com_type = 'KT'
elif (phcom == '019'):
    com_type = 'LGU'
else :
    com_type = '알수없음'
print(com_type)

# 우편번호 
post_num = '01288'
district_num = int(post_num[2])
print(district_num)
district_name = ''
if(district_num in range(0, 3)):
    district_name = '강북구'
elif (district_num in range (3, 6)):
    district_name = '도봉구'
else :
    district_name = '노원구'
print(district_name)


# 주민등록번호 유효성 검사 
regnum = '881225-1235698'
regnum_str = regnum.replace('-', '')

multi_nums = range(2, 10)
sum = 0
for i, n in enumerate(regnum_str):
    if(i > len(multi_nums) -1 ):
        i = i - len(multi_nums)
    sum += int(n) * multi_nums[i]

print(sum % 11)
lastnum = 11 - (sum % 11)
print(lastnum) 


# 비트코인 정보 
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# print(btc)

gap = int(btc['max_price']) - int(btc['min_price'])
# print(gap)
if(int(btc['opening_price']) + gap > int(btc['max_price'])):
    print('상승장')
else:
    print('하락장')


