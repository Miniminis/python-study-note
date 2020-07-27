def prt1():
    print("I'm NiceBoy!")


def prt2():
    print("I'm Goodboy!")


# 단위 실행(독립적으로 파일 실행)
# 해당 모듈만 단위테스트할때 유용하게 사용

if __name__ == "__main__":
    print("This is", dir())
    prt1()
    prt2()
