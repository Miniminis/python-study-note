# if 

if not True:
    pass
else:
    print("true")


score = 90
message = "success" if score >= 60 else "failure"
print(message)

# while
treeHit = 0
while treeHit <10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." %treeHit)
    if(treeHit == 10):
        print("나무 넘어간드아")


# coffee = 10
# while True:
#     money = int(input("커피값을 넣어주시요"))
#     if(money == 300):
#         print("커피 나옵니다.")
#         coffee -= 1
#     elif money >300:
#         print("잔돈 나옵니다.")
#         coffee -= 1
#         change = money-300
#         print(change)
#     else:
#         print("돈이 모자랍니다. 다시 받아가세여")
#         change = money
#         print(change)
#     if coffee == 0:
#         print("잔여 커피가 없습니다.")
#         break

add = 0
for i in range(1, 11):
    add = add + i
print(add)

num = [1, 5, 2, 123]
for i in range(len(num)):
    print(i)
    i = num[i]
    # print(i)

for i in range(2, 10):
    for j in range(1, 10):
        print("{0} * {1} = {2}".format(i, j, i*j))
    print('')

