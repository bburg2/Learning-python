# Here I make a list object and add a few numbers to it
myList = []
myList.append(1)
myList.append(2)
myList.append(3)

# Next I print an object in the list where it is located
print(myList[0])
print(myList[1])
print(myList[2])

# This for loop prints all the objects in list
for x in myList:
    print(x)

# Add another number an print all the objects in the list again
myList.append(4)
for x in myList:
  print(x)
  
# You can't acces an object in a list wich does not exicst
mylist = [1,2,3]
print(mylist[10])
