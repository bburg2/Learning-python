# this is the eleventh excercise and can be found at: https://www.learnpython.org/en/Modules_and_Packages

import re

# Your code goes here
find_members = []
for member in dir(re):
  if "find" in member:
    find_members.append(member)
    
print(sorted(find_members))
