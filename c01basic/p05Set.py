# 집합 자료형 
s1 = set([1,2,3])
print(s1)

s2 = set("minhee")
print(s2)   
# 집합이므로 정렬되지는 않음 - 순서가 없다.
# 중복을 허용하지 않는다. 
# 만약 set 자료형에 저장된 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환한후 해야 한다.

listS2 = list(s2)
listS2.sort()
print(listS2)


s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)
print(s1.intersection(s2))
print(s1 | s2) 
print(s1.union(s2))
print(s1 - s2)
print(s1.difference(s2))

print(s1.add(524))
print(s1)
print(s1.update([233, 123, 827]))
print(s1)

print(s1.remove(2))
print(s1)
