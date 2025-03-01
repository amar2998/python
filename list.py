list=[1,2,3,4,5,6]
print(list[5]) # access
list[2]=33
print(list) # mutable

list.append(23)
print(list)
list.insert(2,4)
print(list)
list.sort()
print(list)
list.sort(reverse=True)

print(list)
list.reverse()
print(list)
list.pop()
print(list)

print(list.index(2))
list2=list.copy()
print(list2)
list2.remove(5)
print(list2)
print(list2.count(4))
print(list.count(4))
list2.clear()
print(list2)


list1=[1,2,3,4]
list2=[4,5,6,7]
list3=list1+list2
print(list3)
