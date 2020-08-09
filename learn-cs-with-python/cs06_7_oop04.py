"""
객체지향프로그래밍으로 은행 입출금 프로그램 만들기
"""

class Account:
    num_acnt = 0           #1

    @classmethod
    def get_num_acnt(cls): #2
        '''
        cls.get_num_acnt() -> integer
        '''
        return cls.num_acnt

    def __init__(self, name, money):
        self.user = name   #3
        self.balance = money
        Account.num_acnt += 1  #4

    def deposit(self, money):
        if money < 0:
             return
        self.balance += money

    def withdraw(self, money):
        if money > 0 and money <= self.balance:
            self.balance -= money
            return money
        else:
            return None

    def transfer(self, other, money):    #5
        '''
        obj.transfer(other, money) -> bool
        other : The object to interact with
        money : money the user wants to send

        returns True if the balance is enough to transfer
        returns False if not
        '''
        mon = self.withdraw(money)
        if mon:
            other.deposit(mon)
            return True
        else:
            return False

    def __str__(self):      #6
        return 'user : {}, balance : {}'.format(self.user, self.balance)


if __name__== "__main__":
    # 객체 생성
    my_acnt = Account('greg', 5000)
    your_acnt = Account('john', 1000)

    # 생성 확인
    print('object created')
    print(my_acnt)
    print(your_acnt)
    print()

    # 인스턴스 메서드를 호출하는 방법
    #1. by object
    my_acnt.deposit(500)            #7
    #2. by class
    # Account.deposit(my_acnt, 500) #8

    # deposit 확인
    print('deposit')
    print(my_acnt)
    print()

    # withdraw 함수 사용법
    print('withdraw')
    money = my_acnt.withdraw(1500)
    if money:
        print('withdrawn money : {}'.format(money))
    else:
        print('Not enough to withdraw')
    print()

    # 클래스 멤버에 접근하는 방법
    print('class member')
    #1.by class
    print(Account.num_acnt)
    #2.by object
    #print(my_acnt.num_acnt)
    print()

    # 클래스 메서드를 호출하는 방법
    print('class method')
    #1.by class
    n_acnt = Account.get_num_acnt()
    #2.by object
    #n_acnt = my_acnt.get_num_acnt()

    print('The number of accounts : {}'.format(n_acnt))
    print()

    # 메시지 패싱
    print("message passing")
    print(my_acnt)
    print(your_acnt)
    res = my_acnt.transfer(your_acnt, 2000)
    if res:
        print('transfer succeeded')
    else:
        print('transfer failed')
    print(my_acnt)
    print(your_acnt)


"""
정적매서드와 클래스 매서드 
정적 매서드 : 인자로 객체나 클래스를 넘겨받지 않음. 일반 함수와 같고 전역함수를 대체하기에 가장 적합
클래스 매서드 : 인자로 클래스를 넘겨받음. 대체생성자로 사용되기도 함
"""

class Person:
      def __init__(self, name, age):             #1
            self.name = name
            self.age = age
      @classmethod
      def init_from_string(cls, string):            #2
            '''
            string format : '<name>_<age>'
            '''
            name, age = string.split('_')
            return cls(name, int(age))                 #3

if __name__ = = "__main__":
      p = Person.init_from_string('greg_30') #4
      print(p.name)
      print(p.age)
