# How can you pick a random item from a list or tuple?


# import the random module
import random

# create a list or tuple (for both it will be the same)
mylist = [1,2,3,4,5,6,7,8,9,10]

# creating a variable to use and store the random item
item = random.choice(mylist)

# printing the item
print(item)