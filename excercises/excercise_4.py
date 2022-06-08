# this is the fourth exercise an can be found at: https://www.learnpython.org/en/String_Formatting
# at first it was hard for me understanding the argument specifiers

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
