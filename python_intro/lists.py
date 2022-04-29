mylist = [1, 2, 3, 4]
myint = 1
mystr = "tacocat"
mybool = True

mylist = [myint, mystr, mybool]

for item in mylist:
    print(item)

print(mylist)


mylist = [1, "two", None, True]
mylist.append("taco")
mylist.append("cat")
print(mylist)
mylist.insert(3, "dog")
print(mylist)

for index, value in enumerate(mylist):
    print(index, value)
