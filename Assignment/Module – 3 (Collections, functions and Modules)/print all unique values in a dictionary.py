# Write a Python program to print all unique values in a dictionary.

# creating a dictionary
my_dict = {'apple': 5, 'banana': 3, 'orange': 5, 'grape': 3, 'pear': 2, 'kiwi': 5}

# creating a set by taking values from the dictionary
unique_values = set(my_dict.values())

# printing the set created
print("Unique values in the dictionary :", unique_values)
