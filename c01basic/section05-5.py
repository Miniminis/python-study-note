# https://wikidocs.net/7028
# 반복문

# 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.
print(' '.join(str(y) for y in range(2002, 2051, 4)))

# 1부터 30까지의 숫자 중 3의 배수를 출력하라.
print(' '.join(str(n) for n in range(1, 31) if n % 3 == 0))

# 구구단 3단을 출력하라.
for n in range(1, 10):
    print('3 * {} = {}'.format(n, 3 * n))

# 
my_list = ["가", "나", "다", "라"]
for i, n in enumerate(my_list):
    if i == len(my_list) -1:
        break
    print(my_list[i], my_list[i+1])




# data에는 매수한 종목들의 OHLC (open/high/low/close) 가격 정보가 바인딩 되어있다.

data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

# 수수료를 0.014 %로 가정할 때, 각 가격에 수수료를 포함한 가격을 한라인에 하나씩 출력하라.

# 2000.28
# 3050.427
# 2050.2870000000003
# ...

arr = []
for row in data:
    for col in row:
        arr.append(col * 1.00014)
print(arr)


