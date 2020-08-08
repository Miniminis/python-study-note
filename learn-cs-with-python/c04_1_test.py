"""
함수 
- 전역변수와 지역변수
"""

# 전역변수 
g_var = 10         #1 전역변수 선언
def func(): 
    print("g_var = {}".format(g_var)) 
if __name__ == "__main__": 
    func() 
# 실행결과 g_var = 10

print()

# 지역변수
g_var = 10       #1 전역변수
def func(): 
    g_var = 20   #2 
    print("g_var = {} in function".format(g_var))  #3: 지역변수
if __name__ == "__main__": 
    func() 
    print("g_var = {} in main".format(g_var))      #4 전역변수 값 출력
# 실행결과 g_var = 20 in function 
#         g_var = 10 in main

print()

# global keyword 를 사용해서 local 매소드 내에서 전역변수를 변경 
g_var = 10            #1 전역변수 선언
def func(): 
    global g_var      #2 전역변수 global 이용해서 함수 내로 가져오기 
    g_var = 20        #3 전역변수 값 변경 
if __name__ == "__main__": 
    print("g_var : {} before".format(g_var))  # 전역변수 10 출력  
    func()                                      # 함수 내에서 전역변수 값 가져와서 변경 
    print("g_var : {} after".format(g_var))     # 바뀐 전역변수 값 20 출력

print()

# nonlocal keyword 이용해서 변수 바꾸기
def outer(): 
    a = 2           #1 a=2, b=3
    b = 3 
    def inner(): 
        nonlocal a  #2 nonlocal 이용해서 inner() 외부에 선언된 a 변수의 값 가져오기
        a = 100     #3 가져온 외부의 a 값 변경 
    inner() # inner 함수 실행
    print("locals in outer : a = {}, b = {}".format(a, b))      # a=100, b=3 
if __name__ == "__main__": 
    outer() 
