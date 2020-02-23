# practice

#01 
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

#02 
num = 1
sum = 0
while num <= 1000:
    if(num%3==0): 
        sum += num
    num += 1
print(sum)

#03 
num = 0
while num <= 5:
    num += 1
    print("*"*num)

#04 
for i in range(1, 101):
    print(i)

#05 
marks = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for i in marks:
    sum += i
print("학급의 평균 점수는 : {0}".format(sum/10))

#06 
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2==1] 
print(result)  