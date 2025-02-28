class cars:
    def __init__(self,name,color,typing,seat):
        self.name=name
        self.color=color
        self.typing=typing
        self.seat=seat
    
    def display(self):
        print(f"the name is {self.name} color is {self.color} type of car is {self.typing} no of seat{self.seat}")



c=cars("tata","red","4wheel",5)
c.display()

class bikes:
    name=""
    ABS=False
    seats=0
    milage=0
    def __init__(self,name,ab,seat,mil):
        self.name=name
        self.ABS=ab
        self.seats=seat
        self.milage=mil

    def display(self,):
        print(self.name)
        print(self.ABS)
        print(self.seats)
        print(self.milage)

    @staticmethod   # it makes the method class member
    def dis():
        print("hello world")


bik=bikes("yamaha",True,2,45)
bik.display()
bik.dis()