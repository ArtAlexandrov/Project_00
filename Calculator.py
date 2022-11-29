import math
class Calculator:
    def __init__(self):
        pass
    def add(self, x1, x2):
        return x1+x2
    def multiply(self, x1, x2):
        return x1*x2
    def subtract(self, x1, x2):
        return x1-x2
    def divide(self, x1, x2):
        if x2 !=0:
            return x1/x2
    def pow(self, x1, x2):
        return x1 ** x2
    def common(self, x1):
        #return math.sqrt(x1)
        if x1 <0:
            return print ("Ошибка")
        if x1 >=0:
            return math.sqrt(x1)