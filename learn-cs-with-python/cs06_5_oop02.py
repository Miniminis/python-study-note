"""
Person 을 클래스로 만들어 객체지향 프로그래밍을 해보자 
속성 = 멤버 + 매서드 
"""

class Person:
    def __init__(self, name, money):
        self.name = name 
        self.money = money 

    def give_money(self, other, money): 
        self.money -= money
        other.get_money(money) 

    def get_money(self, money):
        self.money += money

    def show(self):
        print('{} : {} '.format(self.name, self.money))

if __name__ == "__main__":

    # 객체 생성
    g = Person('greg', 5000)  
    j = Person('john', 2000)

    g.show()
    j.show()
    print('')

    # 메시지 패싱
    g.give_money(j, 2000)     

    g.show()
    j.show()

"""
왜 클래스에서 정의된 매서드에는 인자가 self 가 포함되어있는데, 실제로 인스턴스 생성 및 매서드 호출시에는 self 객체를 넘겨주지 않을까?
- 인스턴스 매서드를 호출하면, 객체가 자동으로 첫번째 인자인 self 로 객체 자신을 전달하기 때문임!
"""


"""
파이썬의 클래스를 좀 더 살펴보자.
"""
print('')

print(">>>Person class")
print(type(Person.__init__))
print(type(Person.give_money))
print(type(Person.get_money))
print(type(Person.show))

print()

print('>>>Instance g and j')
print(type(g.give_money))
print(type(j.get_money))

"""
Person class 내부의 매서드들은 function, instance g 와 j의 매서드들은 method 라고 출력됨을 확인할 수 있다. 
"""

print()

print('>>>')
print(dir(g.give_money))
print(g.give_money.__func__)
print(g.give_money.__self__)

print('>>>')
print(g.give_money.__func__ is Person.give_money)
print(g.give_money.__self__ is g)

"""
instance g 의 give_money method 는 Person 클래스의 give_money() 함수이고 
instance g 의 give_money method 는 객체 자신인 g를 참조하고 있다. 
따라서 매서드 내부에 함수와 객체의 참조를 가지고 있으므로, 매서드 호출 시에 self 를 전달하지 않아도 되는 것이다!
"""
