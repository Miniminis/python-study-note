"""
정보은닉
캡술화 : 관련있는 변수와 매서드를 묶어 클래스로 만들어 내는 것
정보은닉 : 외부에서 접근하지 못하도록 변수나 매서드에 대한 접근성을 제약하는 것
"""

# 파이썬은 정보은닉을 제공하지 않으므로 C++의 정보은닉을 살펴보기로함

class Account{
public: // #1
    // 생성자: 파이썬 클래스의 __init__( )과 같다
    Account(string name, int money){
        user = name;
        balance = money;
    }
    // 인스턴스 메서드(멤버 함수)
    int get_balance() {
        return balance;
    }
    // 인스턴스 메서드(멤버 함수)
    void set_balance(int money) {
        if (money < 0) {
            return;
        }

        balance = money;
    }
private: // #2
    // 인스턴스 멤버(멤버 변수)
    string user;
    int balance; // #3
};


"""
public, protected, private : 접근제어지시자
public : 객체를 만들어 사용하는 쪽에서 접근하거나 호출 가능
private : 클래스 내부에서만 사용할 수 있고 객체를 통해서는 접근이 불가
"""

int main(void){
      Account my_acnt("greg", 5000);

      my_acnt.balance; // #4 컴파일 오류 : balance 는 외부에서 접근 불가

      return 0;
}

"""
정보은닉으로 접근 불가한 멤버에 대해서 접근하는 방법은 바로 엑세스 함수를 이용하는 것. (get or set)
정보은닉을 이용하면 숨긴 멤버에 들어갈 값을 엑세스 함수를 통해서 제어할 수 있다는 장점이 있다. 
위의 예시 같은 경우는 balance 는 항상 set_balance 를 통해서만 접근 가능하기 때문에 음수가 들어가는 것을 예방할 수 있음
"""

"""
파이썬의 정보은닉 
"""

class Account:
    def __init__(self, name, money):
        self.user = name
        self.balance = money

    def get_balance(self):
        return self.balance

    def set_balance(self, money):
        if money < 0:
            return

        self.balance = money

if __name__ == "__main__":
    my_acnt = Account('greg', 5000)
    my_acnt.balance = -3000   #1 balance 멤버에 바로 접근하여 음수값을 대입해버림

    print(my_acnt.get_balance())


"""
파이썬에서는 위에서 보는 바와 같이 정보은닉이 불가능하다. 
하지만 정보은닉처럼 기능하도록 할 수 있는 방법이 2가지 있다. 그러나 완벽한 정보은닉은 아니므로 주의. 
1. 숨기려는 멤버 앞에 언더바( _ )를 두 개 붙이기
2. 프로퍼티 기법
"""

# 1. 숨기려는 멤버 앞에 언더바( _ )를 두 개 붙이기

class Account:
    def __init__(self, name, money):
        self.user = name
        self.__balance = money  #1

    def get_balance(self):
        return self.__balance   #2

    def set_balance(self, money):
        if money < 0:
            return
        self.__balance = money  #3

if __name__ = = "__main__":
    my_acnt = Account('greg', 5000)
    my_acnt.__balance = -3000   #4

    print(my_acnt.get_balance())


"""
위의 코드 출력결과는 5000이다. 정보은닉이 된것처럼 보일 수 있지만, 아래를 확인해보면 그렇지 않다는 것을 알 수 있다. 
"""

print(my_acnt.__dict__)
"""
결과 : {'user': 'greg', '_Account__balance': 5000, '__balance': -3000}

언더바 2개를 붙인 변수는 클래스가 생성되면서 '_클래스__멤버' 라는 이름으로 변하게 된다.
__balance 는 객체 my_acnt의 멤버이다. 

결과적으로 언더바 2개를 붙인 변수는 접근하기가 까다로워져서 개발자의 실수를 막아주지만 
일부러 해당 변수를 수정하려는 움직임까지는 막지 못한다. 
"""



# 2. 프로터티 기법 : 변수에 접근하는 것처럼 보이지만 사실은 매서드를 호출하는 것임 

class Account:
    def __init__(self, name, money):
        self.user = name
        # 인스턴스 멤버 선언이 아니라 #3의 setter 메서드를 호출
        self.balance = money     #1

    @property
    def balance(self):           #2 데코레이터 @property : balance 의 getter 함수처럼 동작
        return self._balance

    @balance.setter
    def balance(self, money):    #3 
        if money < 0:
            return

        # 실제 인스턴스 멤버 선언이 일어나는 부분(#1 실행시(생성자 호출시))
        self._balance = money

if __name__ == "__main__":
    my_acnt = Account('greg', 5000)
    my_acnt.balance = -3000      #4 balance 라는 변수에 직접 접근하지 않고, setter 함수를 통해 접근하므로 음수로 변경되지 않는다.

    print(my_acnt.balance)       #5


"""
하지만 이 방법 역시 'my_acnt.__dict__' 호출을 통해 멤버를 확인할 수 있고 해당 멤버 값에 접근하여 음수로 변경하게 되면 setter 함수를 통해 변경하는게 아니므로 음수값으로 변경이 되어버린다 ㅠㅠㅠ
파이썬에서는 완벽한 정보은닉은 불가능하다. 
"""

