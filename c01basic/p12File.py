# file 
# r: 읽기모드 
# w: 쓰기모드 
# a: 추가모드 

# f = open("newfile.txt", 'w')
# data = "hello, python!"
# f.write(data)
# f.close()

f = open("newfile.txt", 'r')
line = f.readline()
print(line)
f.close()

# f = open("newfile.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

f = open("newfile.txt", 'a')
for i in range(11, 20):
    data = "%d line" % i
    f.write(data)

f = open("newfile.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
print(f.read())     #파일 전체 읽기
f.close()

# with() : 자동 close 
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")

