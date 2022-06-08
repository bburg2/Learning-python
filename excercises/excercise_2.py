# this is the second exercise and can be found at: https://www.learnpython.org/en/Lists

# make a few lists
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# append some numbers to numbers
numbers.append(1)
numbers.append(2)
numbers.append(3)

# append text to strings
strings.append("hello")
strings.append("world")

# write your code here
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
