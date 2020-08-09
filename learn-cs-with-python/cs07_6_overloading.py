"""
연산자 오버로딩
"""

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def set_point(self, x, y):
        self.x = x
        self.y = y

    def get_point(self):
        return self.x, self.y

    def __str__(self):
        return '({x}, {y})'.format(x = self.x, y = self.y)

    
    # 더하기 연산자(+) 오버로딩
    def __add__(self, n):     #1 오버로딩 이후에는 에러 발생하지 않음. (5,5)출력
        x = self.x + n
        y = self.y + n
        return Point(x, y)
    
    def __radd__(self, n):    #1
        x = self.x + n
        y = self.y + n
        return Point(x, y)

if __name__=="__main__":
    p1 = Point(2, 2)
    p2 = p1 + 3               #1  point 객체와 3을 더할 수 없다는 에러 발생 --> 오버로딩 이후에 정상출력
    p3 = 3 + p1               #3 에러발생  

print(p2)
print(p3)


"""
표 7-1 산술 연산자 오버로딩 메서드
메서드 연산자
__add__(self, other) : +
__sub__(self, other) : -
__mul__(self, other) : *
__truediv__(self, other) : /
__floordiv__(self, other) : //
"""

