# while


i=0
while(i<=6):
    print(i)
    i+=1
num=int(input("enter the num of the table"))

i=1
while(i<=10):
    print(num*i)
    i+=1

lis=[1,2,3,4,5,6,7,8,9,10]
size=len(lis)
i=0
while(i<size):
    if(lis[i] == 12):
        print("found it")
        break
    else:
        i+=1

list=[1,2,3,4,5,6,7,8]
tup=(1,2,3,4,56,7,8)
str="hi my name is amar"
for ele in str:
    print(ele,end=" ")
else:
    print("end")

for ele in range(100,0,-1): # start , stop , step
    print(ele)
    
for ele in range(10):
    pass
print("hii")
