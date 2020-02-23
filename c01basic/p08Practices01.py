# practices 

#01 
(kor, eng, math) = (80, 75, 55)
avg = (kor+eng+math)/3
print(avg)

#02
num = 13
print("{0}은 짝수 입니까? - {1}".format(num, (num%2==0)))

#03 
psnum = "881120-1068234"
splits = psnum.split("-")
print(splits[0])
print(splits[1])

#04 
pin = "881120-1068234"
print(pin[7])

#05 
a = "a:b:c:d"
print(a.replace(":", "#"))

#06 
numList = [1, 3, 5, 4, 2] 
numList.sort()
numList.reverse()
print(numList)

#07 
strList = ['Life', 'is', 'too', 'short'] 
completedStr = " ".join(strList)
print(completedStr)

#08 
tup = (1,2,3)
tup1 = (4,)     #tuple 은 요소 1개에도 , 붙여야함
print(tup + tup1)

#09 
a = dict()
print(a)
a['name'] = "python"
print(a)
a[('a',)] = "python"
print(a)
a[250] = 'python'
print(a)
#a[[1]] = "python"   #list 는 변형 가능하기 때문에 key 값으로 쓸 수 없음 
#print(a)

#10 
a = {'A':90, 'B':80, 'C':70}
print(a.pop('B'))

#11 
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(set(a))

#12 
a = b = [1,2,3]
print(a)
print(b)
print(b is a)
a[1]=4
print(a)
print(b)
print(b is a)