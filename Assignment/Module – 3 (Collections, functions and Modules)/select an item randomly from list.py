# Write a Python program to select an item randomly from a list.

# importing random module 
import random

# creating a list
mylist = [111,222,333,444,555,666,777,888,999]

# creating a variable to use random module with choice function to select from list
item = random.choice(mylist)

# printing item
print(item)