# this is the tenth excercise and can be found at: https://www.learnpython.org/en/Dictionaries

phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
# your code goes here

# add Jake
phonebook["Jake"] = 938273443

# remove Jill
del phonebook["Jill"]


# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")  
