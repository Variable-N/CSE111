class Dolls:
    def __init__(self,name,price,quantity = 1):
        self.name = name
        self.price = price
        self.quantity = quantity
    def detail(self):
        if self.quantity == 1:
            return("Doll: "+self.name+"\nTotal Price: "+str(self.price)+" taka")
        else :
            return ("Dolls: "+self.name+"\nTotal Price: "+str(self.price)+" taka")
    def __add__(self,other):
        return Dolls(self.name+' '+other.name,self.price+other.price,2)
    def __gt__ (self,other):
        if self.price > other.price :
            return True
        else :
            return False

obj_1 = Dolls("Tweety", 2500)
print(obj_1.detail())
if obj_1 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_2 = Dolls("Daffy Duck", 1800)
print(obj_2.detail())
if obj_2 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_3 = Dolls("Bugs Bunny", 3000)
print(obj_3.detail())
if obj_3 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_4 = Dolls("Porky Pig", 1500)
print(obj_4.detail())
if obj_4 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_5 = obj_2 + obj_3
print(obj_5.detail())
if obj_5 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")