file=open('textfile.txt',"r") # open and read the file
data=file.read()
print(data)
f=open("module.txt",'w') # remove the previous data  then add new data
f.write(data)

data2="kjshvhfvkhelfjblafvhblkasjhb"
f.write(data2)
f.close()
f2=open('module.txt',"a")
f2.write("\nhi i am amar")
f2.close()
file.close()

op=open('module.txt','r')
print(op.readline())
print(op.readline())
print(op.readline())
op.close()

f=open('textfile.txt','r+')
print(f.read())

f.close()

