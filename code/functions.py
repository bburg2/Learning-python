# functions are definded with "def" followed by the name of the function
def my_function():
    print("Hello From My Function!")

# here I run the function    
my_function()

# functions can also receive arguments
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

# here I run the function with arguments    
my_function_with_args("Bas", "a good day!")

# with return you can return a value
def sum_two_numbers(a, b):
    return a + b
  
# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
print(x)


