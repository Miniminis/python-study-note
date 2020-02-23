# class

class Calculator:
    def __init__(self, first, second):  # 생성자
        self.first = first
        self.second = second    
    def setdata(self, first, second):   # setter
        self.first = first
        self.second = second 
    def add(self):
        return self.first + self.second
    def sub(self):
        return self.first - self.second
    def mul(self):
        return self.first * self.second
    def div(self):
        return self.first / self.second
    
a = Calculator(3, 8)
# a.setdata(4, 8)
print(a.add())
print(a.mul())

# Inheritance 
class MoreFourCal(Calculator):
    def pow(self):
        return self.first ** self.second

b = MoreFourCal(10, 12)
print("="*40)
print(b.add())
print(b.sub())
print(b.mul())
print(b.div())
print(b.pow())

# Overriding 
class SafeFourCal(Calculator):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

c = SafeFourCal(5, 0)
print(c.div())