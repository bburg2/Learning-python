# the % operator can make two objects a tuple ( a fixed size list)
# %s and %d are argument specifiers
# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# "%s" is used to make mylist a string
# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

# here are some basic argument specifers

#%s - String (or any object with a string representation, like numbers)

#%d - Integers

#%f - Floating point numbers

#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

#%x/%X - Integers in hex representation (lowercase/uppercase)

