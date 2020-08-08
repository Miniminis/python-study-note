"""
정수
2진수로 표현 : bin()
16진수로 표현 : hex() 
    메모리 주소를 나타낼 때는 16진수 사용 : 2진수 8자리 == 16진수 2자리 
    32비트 컴퓨터는 32자리 2진수로 나타내는 것이 아니라, 8자리 16진수로 나타냄 
"""

# 10 to 2
print(bin(25))  # 0b11001

# 16 to 2
for i in range(1, 17):
    print(bin(i), end=' ')

print()

# 16 to 2 (2)
list = [0xa, 0xb, 0xc, 0xd, 0xe, 0xf]
for n in list:
    print(bin(n), end=' ')

print()

# 음수표현
# -4 라는 정수를 컴퓨터 메모리에 저장되는 바이트 형태로 표현하는 코드! 
# 몇바이트로 나타낼 것인지, 빅엔디언 or 리틀 엔디언, 양수와 음수를 모두 표현할지 아니면 양수만 표현할지 
num = (-4).to_bytes(1, byteorder='little', signed=True)
print(num)

