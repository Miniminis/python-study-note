# 리스트 안에는 어떠한 자료형도 포함시킬 수 있다.
a = [1, 2, 3]
print(a)
print(a[0])
 
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[-1][0])

a = [1, 2, 3]
print(a*3)

print(len(a))

# print(a[2] + "hi")  #type error 
print(str(a[2]) + "hi")  

# 수정, 삭제
a[1] = 1024
print(a)

del a[1]
print(a)

del a[1:]
print(a)

# 기타함수 
# append, sort, reverse, index, insert, remove, pop, count, extend 