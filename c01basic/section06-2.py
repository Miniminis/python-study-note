# function

def hello(world):
    print('hello~', world)

hello('Mike')

# 다중리턴
def func_mull(x):
    y1 = x*2
    y2 = x*4
    y3 = x*6
    return y1, y2, y3

v1, v2, v3 = func_mull(4)
print(v1, v2, v3)
print(func_mull(2))


# *args, **kwargs 이해
def args_func(*args):  # 매개변수명 자유롭게 변경 가능
    for i, v in enumerate(args):
        print('{}'.format(i), v, end=' ')


args_func('Kim')
args_func('Kim', 'Park')
args_func('Kim', 'Park', 'Lee')

print()


# kwargs
def kwargs_func(**kwargs):  # 매개변수명 자유롭게 변경 가능
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v], end=' ')


kwargs_func(name1='Kim')
kwargs_func(name1='Kim', name2='Park')
kwargs_func(name1='Kim', name2='Park', name3='Lee')

print()


# 전체 혼합
def example(arg_1, arg_2, *args, **kwargs):
    print(arg_1, arg_2, args, kwargs)


example(10, 20, 'park', 'kim', 'lee', age1=33, age2=34, age3=44)


# 힌트
def tot_length1(word: str, num: int) -> int:
    return len(word) * num

print('hint exam1 : ', tot_length1("i love you", 10))


# 람다식
def func_final(x, y, func):
    print(x * y* func(10))
    print(x, y, func(10))

func_final(2, 2, lambda x: x *10)
