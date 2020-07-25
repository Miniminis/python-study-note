# function
# https://wikidocs.net/23906

# math.ceil(i) : 올림
# math.floor(i) : 내림
# math.trunc(i) : 버림
# round()


# 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
def calc_monthly_salary(annual_salary):
    print(round(annual_salary / 12))

calc_monthly_salary(12000000)



# 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.

# make_list("abcd")
# ['a', 'b', 'c', 'd']

def make_list(str):
    return list(str)

print(make_list('flash'))


# 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.
# pickup_even([3, 4, 5, 6, 7, 8])
# [4, 6, 8]

def pickup_even(list):
    return [i for i in list if i % 2 == 0]

print(pickup_even([4, 2, 10, 445, 30, 31]))


