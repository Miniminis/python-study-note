# 2.  has-a 관계 : 합성과 통합

# 합성 : cpu, ram - computer

class CPU:
    pass

class RAM:
    pass

class Computer:
    def __init__(self):
        self.cpu = CPU()  #1
        self.ram = RAM()

"""
computer 가 만들어질때 cpu 와 ram 이 같이 만들어지고, computer 가 없어질때 같이 사라진다. 
--> 합성의 관계
"""


# 통합의 관계 : gun - policeman 

class Gun:
    def __init__(self, kind):
        self.kind = kind

    def bang(self):
        print('bang bang!')

class Police:
    def __init__(self):
        self.gun = None          #1 최초로 경찰이 될 때에는 총이 없는 상태

    def acquire_gun(self, gun):  #2 이 매서드를 통해 총을 소지할 수 있고 
        self.gun = gun

    def release_gun(self):       #3 이 매서드를 통해 총을 반납한다. 
        gun = self.gun
        self.gun = None
        return gun

    def shoot(self):              #4 총이 있으면 방아쇠를 당기고, 없으면 메시지를 출력 
        if self.gun:
            self.gun.bang()
        else:
            print("Unable to shoot")


if __name__ == "__main__":
    p1 = Police()                 #4
    print('p1 shoots')

    p1.shoot()
    print('')

    # p1은 아직 총을 소유하지 않음.
    revolver = Gun('Revolver')

    # p1이 revolver를 획득
    p1.acquire_gun(revolver)      #5
    
    # 이제 p1이 총을 소유하므로
    # revolver는 None이 된다.
    revolver = None
    print('p1 shoots again')
    p1.shoot()
    print('')

    # p1이 총을 반납했으므로
    # 더 이상 총을 소유하지 않는다.
    revolver = p1.release_gun()   #6
    print('p1 shoots again')
    p1.shoot()
