# Write a Python script to check if a given key already exists in a dictionary.

# create a dictionary
my_dict = {"one": 1, "two":2, "three":3}

# we can use in keyword to check if key exist or not
if "one" in my_dict:
    print("one is in the dictionary")

if "six" in my_dict:
    print("six is in the dictionary")
else:
    print("six is not in the dictionary")


# we can also use get() method to check if key exist or not
if my_dict.get("ten") is not None:
    print("Yes it is in dictionary")
else: 
    print("It does not exist in the dictionary")