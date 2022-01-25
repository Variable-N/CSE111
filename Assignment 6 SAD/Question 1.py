class Calculator:
    def __init__(self):
        print('Lets Calculate!')
        self.value1 = None
        self.op = None
        self.value2 = None
    def add (self):
        return self.value1+self.value2
    def subtract (self) :
        return self.value1-self.value2
    def multiply (self) :
        return self.value1*self.value2
    def divide (self) :
        return self.value1/self.value2

obj = Calculator()
obj.value1 = int(input('Value1: '))
obj.op = input('Operator: ')
obj.value2 = int(input('Value2: '))
if obj.op == '+':
    print("Result:",obj.add())
elif obj.op == '-':
    print("Result:",obj.subtract())
elif obj.op == '*':
    print("Result:",obj.multiply())
else :
    print("Result:",obj.divide())