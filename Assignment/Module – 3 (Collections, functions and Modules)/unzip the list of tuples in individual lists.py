# Write a Python program to unzip a list of tuples into individual lists.

# creating a list of tuples
main_list = [(1,"one"),(2,"two"),(3,"three"),(4,"four"),(5,"five")]

# unzip the list of tuples into individual lists
num,let = zip(*main_list)

# print the individual lists
print(num)
print(let)