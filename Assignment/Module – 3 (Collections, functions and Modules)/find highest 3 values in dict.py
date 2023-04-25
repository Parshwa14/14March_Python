# Write a Python program to find the highest 3 values in a dictionary

# create a dictionary
my_dict = {"a" : 200, "b" : 400, "c" :100, "d" : 200, "e" : 500 }

# get the values from dictionary
values = my_dict.values()
# sorting the value in descending order
sort_val = sorted(values, reverse=True)

# to print only first 3 elements
highest_val = sort_val[:3] 

# print(highest_val)
print(highest_val)