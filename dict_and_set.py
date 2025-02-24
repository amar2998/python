dict={
    "key1":23,
    "key2":34,
    "key3":54
}
# print(dict)


dict2={
    "strkey":"hello",
    2:"amar sonu nath",
    3:23,
    True:"value is er",
    "tuple":(1,2,3,4,5),
    "list":[1,2,3,4,5],
    "dict":{
        "key1":23,
        "key2":34,
    }
}
#mutable
dict2["strkey"]="hello world"

print(dict2)
print(dict2["list"][4])
print(dict2.get("list")[4]) # get the value of key

print(dict2.get(2)) # get the value of key
to get all keys
print(dict2.keys())
print(dict2.values())
print(dict2.items())
print(len(dict2["list"]))
print(len(list(dict2[True])))
print(dict2.get("tuple"))
print(dict2["dict"].update({"key1":45}))
print(dict2["dict"])


set
set={1,2,3,4,5,5,5,5,67} #unordered and random 
set.add(99)
set.add("amar")
set.remove(99)
set.clear()
set.update([1,2,3,4,5,6,7,8,9,10])
set.pop()
set.pop()
set.pop()
print(set)


set4={1,2,3,4}
set5={2,3,11,12}
print(set4.union(set5))
print(set4.difference(set5)) # it will remove only those value which are comman in both the set ant will only
#  remove in set4 and give the remaining value in set 4

print(set4.symmetric_difference(set5))#it will remove the comman value in both the set and give the remaining value in both the set
print(set4.intersection(set5))

dict={
    "table":["a piece of furniture ","list of fact and figures"],
    "cat":"a small domesticated animal"
}
print(dict)

class1={"python","java","javascript","c++","python"} # stes are also random and unordered
class2={"java","python","c","c++","java"}
class3=class1.union(class2)
print(class1)