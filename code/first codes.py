# print a line
print("This line will be printed.")

# an if statetement doesn't need curly braces
x = 2
if x == 2:
    # indented four spaces
    print("x is not 1.")

# Every variable in Python is an object
myint = 7
print(myint)

# a float is a number with decimals
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# strings are defined either with a single quote or a double quotes
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

# double quotes make it easier for apostrophes
mystring = "Don't worry about apostrophes"
print(mystring)

# you can add object to each other
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# assignments for more than one variable
a, b = 3, 4
print(a, b)

# mixing numbers and strings doesnt work
one = 1
two = 2
hello = "hello"

print(one + two + hello)
