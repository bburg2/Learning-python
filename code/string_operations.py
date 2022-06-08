astring = "Hello world!"
print("single quotes are ' '")

# you can print the length of a string with len()
print(len(astring))

# print the location of the first ocurence of letter o, o is at 4 because python starts counting at 0
print(astring.index("o"))

# counts the number of l in the string
print(astring.count("l"))

# prints l
# the general form is: [start:stop:step]
print(astring[3:7:2])

print(astring[3:7])
print(astring[3:7:1])

# to reverse the string
print(astring[::-1])

# print upper or lower case
print(astring.upper())
print(astring.lower())

# see if the string start with something or ends with something: output is TRUE or FALSE
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

# make a list of the string where the string is spiced with a space
afewwords = astring.split(" ")
print(afewwords)
