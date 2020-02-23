# Variables 

a = [1,2,3]
print(id(a))

# 같은 리스트 값을 다른 변수에 할당 : 결론적으로 id 값 같음 
b = a
print(id(a))
print(id(b))
print(b is a)

# 리스트를 복사 : id 값이 다름 
b = a[:]
print(id(a))
print(id(b))
print(b is a)

c = a.copy()
print(id(a))
print(id(c))
print(c is a)

