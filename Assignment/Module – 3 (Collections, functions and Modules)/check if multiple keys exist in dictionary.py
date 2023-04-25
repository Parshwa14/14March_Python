# Write a Python program to check multiple keys exists in a dictionary.

# creating a dictionary
my_dict = {'apple': 5, 'banana': 7, 'orange': 9, 'grape': 3}

# list of keys to check in the keys
keys_to_check = ['apple', 'banana', 'watermelon']

# check by using (if, all) that keys exist in the dictionary
if all(key in my_dict for key in keys_to_check):
    print("All keys exist in the dictionary")
else:
    print("At least one key does not exist in the dictionary")
