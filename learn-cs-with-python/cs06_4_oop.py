"""
객체지향프로그래밍
- 객체 : 고정된 형태나 모양이 있어서 만지거나 볼 수 있는 것. 사람, 동물, 물건 등 
- 객체지향프로그래밍 : 현실세계에 존재하는 객체를 모델링하여 프로그래밍하는 것
"""

"""
캡슐화
- 객체가 지니는 특징은 변수로, 행동이나 기능은 함수로 표현하여 하나의 단위(클래스)로 묶는 것
- 예를 들면, 사람이라는 클래스에는 키, 몸무게, 직업, 성별 등의 특성이 변수로 표현될 수 있으며 잠자기, 숨쉬기와 같은 행동이 함수로 표현될 수 있다. 
- 이러한 클래스에 대한 객체로 나, 히로시, 에이미 등 많은 사람들이 표현될 수 있다. 
"""    

"""
우선, 클래스를 사용하지 않고 객체지향으로 프로그래밍을 해보자.
"""

# 인스턴스 멤버 초기화
def person_init(name, money):
    obj = {'name' : name, 'money' : money} #1
    obj['give_money'] = Person[1]          #2
    obj['get_money'] = Person[2]
    obj['show'] = Person[3]
    return obj

def give_money(self, other, money): #3
    self['money'] -= money
    other['get_money'](other, money) #4 두 사람간의 상호작용이 일어남. 메시지 패싱.

""" 
서로 다른 객체가 함수호출을 통해 상호작용하여 객체의 상태(데이터)가 변하는 것을 메시지 패싱이라고 한다. 
"""

def get_money(self, money):
    self['money'] += money

def show(self):
    print('{} : {}'.format(self['name'], self['money']))


if __name__ == "__main__":
    Person = person_init, give_money, get_money, show

    # 객체 생성
    g = Person[0]('greg', 5000) #5
    j = Person[0]('john', 2000)

    g['show'](g)
    j['show'](j)
    print('')

    # 메시지 패싱
    g['give_money'](g, j, 2000)     #6

    g['show'](g)
    j['show'](j)

