# Write a Python script to merge two Python dictionaries.

# creating two dictionaries
dict1 = {"one" : 1, "two" : 2, "three" : 3}
dict2 = {"four" : 4, "five" : 5, "six" : 6}

# creating a dictionary for merging 
# copying dict1 to comb_dict
comb_dict = dict1.copy()
# updating dict2 in comb_dict 
comb_dict.update(dict2)

# print the combined dictionary
print(comb_dict)