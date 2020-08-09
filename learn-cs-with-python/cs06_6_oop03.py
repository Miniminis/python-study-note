"""
클래스 멤버와 매서드
"""

class A:
    c_mem = 10           #1 클래스 변수(멤버)

    @classmethod
    def cls_f(cls):      #2 클래스 매서드(데코레이터로 설정)
        print(cls.c_mem)

    def __init__(self, num):
        self.i_mem = num #3

    def ins_f(self):
        print(self.i_mem)

if __name__ == "__main__":
    print(A.c_mem)               #4
    A.cls_f()                    #5

    a = A(20)      #6
    print(a.c_mem) #7
    a.cls_f()      #8

"""
아직 인스턴스를 생성하지 않았음에도 클래스 멤버와 매서드에 접근할 수 있음을 알 수 있다. 
뿐만 아니라 객체에서도 클래스 멤버와 매서드에 접근할 수 있다. 
모든 객체가 클래스 멤버를 공유한다!
"""
