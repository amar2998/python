class car:
    def start(self):
        print("car hs started")

    def stop(self):
        print("car has stopped")

class Tata(car):
    def __init__(self,name):
        self.name=name

    def display(self):
        print(self.name)

car1=Tata("safari")
car1.display()
car1.start()
car1.stop()
class main:
    data="i need it"
    @classmethod
    def display(cls):
        print(cls.data)


cl=main()
cl.display()


class student:
    def __init__(self,phy,math,chem):
        self.phy=phy
        self.math=math
        self.chem=chem
    @property # this will convert the function to an attribute or variable with the returning value to its value
    def percentage(self):
        return (self.phy+self.chem+self.math)/3
amar=student(90,98,89)

print(amar.percentage)
amar.chem=100
print(amar.percentage)