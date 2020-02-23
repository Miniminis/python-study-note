# 정수, 실수, 8진수(0o), 16진수(0x)
# +, -, *, /, // 몫, % 나머지, ** 제곱 

# ** 연산자 
a = 10
b = 5
print(a ** b) 

# //와 % 연산자 
print(a//b)
print(a%b)

# 문자열 연산 
print("="*50)
print("hello, python!")
print("="*50)

# 문자열 길이 
str = "Life is too short, you need python"
print(len(str))

# 문자열 슬라이싱 
print(str[0:4])     # 0 <= a < 4
print(str[5:7])
print(str[12:17])
print(str[19:])
print(str[:17])
print(str[:])
print(str[19:-7])

# 정렬과 공백
print("===정렬과 공백===")
print("%10s" %"hello")
print("%-10ssix" %"mashim")

print("="*50)
print("%0.4f" % 3.42134234)     #4자리까지만 나타냄
print("%10.4f" %3.43143234)     


# format () 
print("hello, {}".format("python!"))
print("i ate {0} apples and {1} orange juice".format(13, "drank"))

# format(name="")
print("what a beautiful {noun}".format(noun="day"))

# 정렬 
print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:!<10}".format("hi"))
print("{0:=^10}".format("hi"))


# f문자열 포메팅 
name="홍길동"
nickname = "홍당무"
age = 27 
print(f"나의 이름은 {name} 입니다. 별명은 {nickname} 이지요.")
print(f"나의 이름은 {name} 입니다. 내년에는 {age+1} 살이 되지요.")


# 관련함수들 
print(str.count('i'))
print(str.find('i'))    # 존재 : index
print(str.find('k'))    # 존재하지 않으면 -1
print(str.index('i'))   # 존재하면 index
# print(str.index('k'))   # 존재하지 않으면 error
print(".".join(str))
print(",".join(['a', 'b', 'c', 'd']))
print(str.upper())
# str = "LIFE"
print(str.lower())
print(str.replace("Life", "Groomy"))
print(str.split())  #공백기준
print(str.split(","))