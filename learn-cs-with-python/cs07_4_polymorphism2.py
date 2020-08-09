"""
다형성2
"""

# class Animal:
#     def eat(self):              #1
#         print('eat something')

from abc import abstractmethod, ABCMeta

class Animal(metaclass = ABCMeta):  #2
    @abstractmethod
    def eat(self):                
        pass

class Lion(Animal):
    def eat(self):              #2
        print('eat meat')

class Deer(Animal):
    def eat(self):              #3
        print('eat grass')

class Human(Animal):
    def eat(self):              #4
        print('eat meat and grass')

class Pig(Animal):
    pass

if __name__ == "__main__":
    animals = [ ]               #5
    animals.append(Lion())
    animals.append(Deer())
    animals.append(Human())
    # animals.append(Pig())     # eat() 오버라이딩 없이 상속받을 수 없다.


    for animal in animals:
        animal.eat()            #6 다형성

    # a = Animal()    # 추상클래스에 대해 인스턴스를 만들 수 없다고 오류남

"""
eat meat
eat grass
eat meat and grass
"""


"""
세상에 무엇인가 먹는 동물은 없고, 항상 특정한 것을 먹으므로 Animal 클래스에 대한 인스턴스를 아예 생성 못하게 막고 싶음
--> 추상클래스 
"""



"""
클래스 설계시 유의사항 
1| 공통 부분을 기본 클래스로 묶는다. 이렇게 하면 코드를 재사용할 수 있다.
2| 부모가 추상 클래스인 경우를 제외하고, 파생 클래스에서 기본 클래스의 여러 메서드를 오버라이딩한다면 파생 클래스는 만들지 않는 것이 좋다.
"""