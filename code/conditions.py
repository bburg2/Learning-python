# python uses boolean value to evaluate conditions, asignig a value is done with ("="), comparing two variables is done with ("=="). 
# the "not equals" operator is marked as "!="
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

# python also has "and" and "or" operators
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
    

# with the "in" operator you can check if a specified object exist within an itarable object, such as list
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
    
# python doesn't use brackets    
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    print("%s is True" % another_statement)
    pass
else:
    # do another thing
    pass
  

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")
    
# "is" matches the instances themselves?   
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

# using not before a boolean inverts it
print(not False) # Prints out True
print((not False) == (False)) # Prints out False
