# class man:
#     def __init__(self,inte,int2):
#         self.var1=inte
#         self.var2=int2

#     def display(self):
#         print(self.var1)
#         print(self.var2)

# clas=man("amar","sonu")
# clas.display()
# del(clas) # delete the instance

class Account:
    def __init__(self,data1,data2):
        self.AccountNo=data1
        self.__pass=data2
    def display(self):
        print(self.AccountNo)
        self.__display2() # calling private function


    def __display2(self):
        print(self.__pass)

ob1=Account(12345,'amar123*')
ob1.display()


