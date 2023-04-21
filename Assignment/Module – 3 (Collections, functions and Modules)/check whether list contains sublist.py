# Write a Python program to check whether a list contains a sub list

# creating a main list and sub list
main_list = [1,2,3,4,5,6]
sub_list = [1,5]

# converting the lists to set to check 
main_set = set(main_list)
sub_set = set(sub_list)


# using issubset method of set to check 
if sub_set.issubset(main_set):
    print("Yes, list contains sub list")

else:
    print("NO, list does not contain sub list")

