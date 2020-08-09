"""
다형성: 상속관계에 있는 다양한 클래스의 관계에서 같은 이름의 매서드를 호출할 때, 각 객체가 서로 다르게 구현된 매서드를 호출함으로써 서로 다른 행동, 기능, 결과를 가져오는 것
매서드 오버라이딩 : 파생 클래스 안에서 상속받은 매서드를 다시 구현하는 것
"""

class CarOwner:
    def __init__(self, name):
        self.name = name

    def concentrate(self):
        print('{} can not do anything else'.format(self.name))
    # 나머지 메서드

class Car:
    def __init__(self, owner_name):
        self.owner = CarOwner(owner_name)

    def drive(self):              #1
        self.owner.concentrate()  #2
        print('{} is driving now.'.format(self.owner.name))  #3

    # 나머지 메서드

class SelfDrivingCar(Car):
    def drive(self):                       #4
        print('Car is driving by itself')  #5

if __name__ == "__main__":
    car = Car('Greg')
    car.drive()           #6
    print('')

    s_car = SelfDrivingCar('John')
    s_car.drive()         #7

"""
실행결과 :
Greg can not do anything else
Greg is driving now.

Car is driving by itself

같은 이름의 매서드를 호출해도 다른 결과를 가져온다. --> 다형성!
"""