"""
함수 : 인자전달방식에 따른 분류
1. 값
2. 참조
3. 객체참조
"""

# 1. 값에 의한 인자 전달 
include <iostream>
using namespace std;

void change_value(int x, int value) // #3 change_value() 함수 정의 
{
    x = value;                      // #4 전달받은 x 값을 value 값으로 변경 
    cout << "x : " << x << " in change_value" << endl;  //#5 함수 내에서 x 값 확인
}

int main(void)
{
    int x = 10;                     // #1 변수 x 선언
    change_value(x, 20);            // #2 change_value() 함수 호출, x값 넘겨주기 
    cout << "x : " << x << " in main" << endl;  //#6 메인에서 x 값 확인

    return 0;
}


"""
실행결과 
x : 20 in change_value
x : 10 in main

함수 내에서 출력한 내용은 변했는데, 메인 함수에서 다시 확인해보니 변수 x 값은 그대로이다.
이유는 변수 x를 전달한 것이 아니라, x의 값을 전달했기 때문. 

* 스택프레임 개념 
함수가 호출될 때 메모리 내에서는 "스택프레임"이 생긴다. 
함수 내에 정의되어있는 변수들이 메모리를 차지하는 공간이 생기고
함수가 호출되는 순서에 따라서 차곡차곡 위로 쌓인다 --> 스택구조로!
그래서 제일 나중에 호출된 함수가 가장 먼저 사라지고, 제일 먼저 호출된 함수는 가장 나중에 사라지게 된다.
"""


# 2. 참조에 의한 인자 전달
include <iostream>
using namespace std;

void change_value(int *x, int value) // #3 change_value() 함수 정의
{
    *x = value;                       // #4 포인터 변수 x로 main 함수의 x가 참조하고 있는 메모리의 주소를 찾아서 value 값을 삽입 
    cout << "x : " << *x << " in change_value" << endl; // #5 함수 내에서 x값 출력
}

int main(void)
{
    int x = 10;                       // #1 변수 x정의
    change_value(&x, 20);             // #2 change_value() 함수 호출 : 인자로 변수 x가 차지하고 있는 메모리 주소의 첫번재 바이트를 전달(포인터변수)
    cout << "x : " << x << " in main" << endl;      //#6 main 함수 내에서 x값 출력
    return 0;
}


"""
실행결과
x : 20 in change_value
x : 20 in main

포인터 변수를 통해서 메모리주소값을 직접 넘겨서, 함수내에서 메인함수에 정의된 변수의 값을 변경하였다!!!
"""


# 3. 객체참조에 의한 인자 전달(변경불가능객체전달)
def change_value(x, value):   #3 change_value() 함수 정의
    x = value                 #4 x값을 value 로 변경
    print("x : {} in change_value".format(x))   #5 x = 20

if __name__ = = "__main__":
    x = 10                    #1 변수 x 선언
    change_value(x, 20)       #2 change_value() 호출
    print("x : {} in main".format(x))   #6 x=10

"""
실행결과 
x : 20 in change_value 
x : 10 in main

파이썬의 경우는 C언어처럼 변수 내부의 값을 담고 있는 형태가 아니라, 메모리에 저장되어있는 값을 참조하는 형태.
변수 이름은 값을 가리키는 형태이다!
"""

# 4. 객체참조에 의한 인자 전달(변경가능객체전달)
def func(li):
    li[0] = 'I am your father!'   #3. func() 정의, 전달받은 리스트의 요소 변경 시도

if __name__ = = "__main__":
    li = [1, 2, 3, 4]       #1. list 정의
    func(li)                #2. func() 호출
    print(li)               #4. list 요소 확인을 위해서 print() 

"""
실행결과 ['I am your father!', 2, 3, 4]

리스트의 요소를 직접 참조하여 변경했기 때문에 리스트가 변경됨
"""

def func(li): 
    li = ['I am your father', 2, 3, 4]   #1 
if _ _name__ = = "__main__": 
    li = [1, 2, 3, 4] 
    func(li) 
    print(li) 

"""
실행결과 [1, 2, 3, 4]
아예 새로운 리스트를 정의한 경우는 main 함수의 li의 요소를 바꾼 것이 아니기 때문에 예외.
"""

