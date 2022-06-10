# dictionary is similar to arrays, but works with keys and values instead of indexes
# values stored in a dictionary can be accesed using a key.
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

# a dictionary can also be made with this method
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

# to iterate over a dictionary use .items()
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# remove values using del  
del phonebook["John"]
print(phonebook)

# or
phonebook.pop("Jack")
print(phonebook)
