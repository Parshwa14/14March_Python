# Write a Python script to concatenate following dictionaries to create a new one.

# creating dictionaries
dict1 = {1:1,2:2}
dict2 = {3:3,4:4}

# creating an empty dictionary to add these two in
my_dict = {}

# using update method from the dictionary to concatenate
my_dict.update(dict1)
my_dict.update(dict2)

# printing the dictionary after concatenation
print(my_dict)