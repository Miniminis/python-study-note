# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for weather in q1.keys():
    if(weather == "가을"):
        print(q1[weather])

# 개선
print(''.join(q1[v] for v in q1 if v == "가을"))
print()

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for v in q2.values():
    if(v == "사과"):
        print("포함됨")
        break
else : 
    print("포함안됨")

# 개선
hasApple = ["사과포함됨!" for k, v in q2.items() if k == '사과' or v == '사과']
if(len(hasApple)>0):
    print('사과있음')
else:
    print('사과없음..')
print()

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

score = 45

if(score > 80 and score <= 100):
    print("A학점")
elif(score > 60 and score <= 80):
    print("B학점")
elif(score >40 and score <= 60):
    print("C학점")
elif (score > 20 and score <= 40):
    print("D학점")
else:
    print("E학점")

# 개선
score = 100
grade = ''

if(score < 0 or score > 100):
    grade = '넌누구니'
elif(score >80):
    grade = 'A'
elif(score >60):
    grade = 'B'
elif(score >40):
    grade = 'C'
elif(score >20):
    grade = 'D'
else:
    grade = 'E'
print('제 점수는요 ... {}'.format(grade))
print()

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용)
a, b, c = 12, 6, 18

max = a
if(b>a):
    if(b>c):
        max = b
    else:
        max = c
else :
    if(a>c):
        max = a
    else:
        max = c
print(max)

# 개선
max = a
if(b>a):
    max = b
if(c>b):
    max = c
print('4. 제일 큰 숫자는요...{}'.format(max))
print()

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
regnum = 9612153569854
gender_num = str(regnum)[6]
print(gender_num)

if(int(gender_num) == 1 or int(gender_num) == 3):
    print("남자")
else:
    print("여자")

# 개선
regnum = 9612153569854
gender_num = str(regnum)[6]
if(int(str(regnum)[6]) % 2 == 0):
    print('여자')
else:
    print('남자')
print()

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for v in q3:
    if(v == "정"):
        continue
    else:
        print(v)

# 개선
print(''.join(s for s in q3 if s != '정'))
print()

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for i in range(1, 100, 2):
    print(i)

# 개선
print(' '.join(str(i) for i in range(1, 100, 2)))
print()

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
for word in q4:
    if(len(word)>=5):
        print(word)

# 개선
print(' '.join(s for s in q4 if len(s) >= 5))
print()

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for char in q5:
    if(char.islower()):
        print(char)

print(' '.join(c for c in q5 if c.islower()))
print()

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for c in q6:
    if(c.islower()):
        print(c.upper())
    else:
        print(c.lower())

print()

print([c.lower() if c.isupper() else c.lower() for c in q6])