"""
*53분*

클래스 
1. is-a 관계 : 상속
2. has-a 관계
"""

# 1. is-a 관계 : 상속

class Computer:
    def __init__(self, cpu, ram):
        self.CPU = cpu
        self.RAM = ram

    def browse(self):
        print('browse')

    def work(self):
        print('work')


class Laptop(Computer):                    #1 Computer 상속
    # 멤버 추가
    def __init__(self, cpu, ram, battery):
        super().__init__(cpu, ram)       #2  Computer 부모 클래스가 가지고 있는 멤버변수와 매서드를 상속받음
        self.battery = battery             #3 Laptop 만의 멤버 추가
    # 메서드 추가
    def move(self, to):                    #4  Laptop 만의 매서드 추가
        print('move to {}'.format(to))


if __name__ == "__main__":
    lap = Laptop('intel', 16, 'powerful')
    lap.browse()       #5 super 를 통해 상속받은 browse 매서드를 호출
    lap.work()
    lap.move('office') #6 새롭게 정의한 move 매서드로 호출


