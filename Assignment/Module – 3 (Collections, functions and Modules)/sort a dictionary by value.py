# Write a Python script to sort (ascending and descending) a dictionary by value.

# create a dictionary
my_dict = {"four" : 4, "one" : 1,  "three" : 3,  "five" : 5, "two" : 2}

# sorting in ascending and descending order using sorted and lambda function
sort_dict_asc = dict(sorted(my_dict.items(),key = lambda x: x[1]))

sort_dict_dsc = dict(sorted(my_dict.items(),key = lambda x: x[1],reverse=True))

# printing the sorted dictionaries
print(sort_dict_asc)
print(sort_dict_dsc)