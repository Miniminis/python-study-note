# function 

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

print(add_mul("mul", 1, 2, 3, 4, 5))

def add_and_mul(a,b): 
    return a+b, a*b

rs1, rs2 = add_and_mul(7, 10)
print(rs1)
print(rs2)

# lamda 
add = lambda a, b: a+b 
result = add(3, 7)
print(result)

# input()
# a = input("강아지의 이름을 대라")
# print(a)

# print()
print("python", "is", "simple")
print("python"+"is"+"simple")
print("python" "is" "simple")

for i in range(10): 
    print(i, end=" ")



