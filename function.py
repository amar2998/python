def add(one,two=6): # right to left default argument
    return one+two

print(add(1))

def converter(val=1):
    return val*83

print(converter(23))


# recurtion
def recur(val):
    if(val==0):
        return
    else:
        recur(val-1)
        print(val)

recur(34)
def fib(n):
    if(n==0 or n==1):
        return 1
  
    else:
        return fib(n-1)+fib(n-2)

print(fib(4))