# classes are a template to create your objects?

# a basic class
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

# assign the class to an object
myobjectx = MyClass()

# to acces te variable inside the class
print(myobjectx.variable)

myobjectx = MyClass()
myobjecty = MyClass()

# you can change to variable when assigning an object
myobjecty.variable = "kaas"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)

# to acces a function inside of a class
myobjectx.function()

# __init__ is a special function that is called when te class is being initiated
class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'
