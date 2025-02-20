string = "amar sonu nath"
print(string[0])
# string[0]='u'#immutable

#method
print(string.capitalize())
print(string[4:]) #slice

print(string.replace("nath","math"))

print(string.upper())
print(string.lower())
str="    stringthis is    "
print(len(str));
str=str.strip() # remove whitespace from front and back
print(len(str));
str2=string+str
print(str2)
print(str.join(string))
# fstring
age=34
name=f"my name is amar and i am {age} years old "
print(name)
print(string.count("a"))
print(string.startswith('a'))
print(string.endswith('a'))
print(string.encode(encoding="ascii",errors="backslashreplace"))
print(string.swapcase())
print(string.index('a'))
print(string.find("amar"))
print(string.split(" "))


