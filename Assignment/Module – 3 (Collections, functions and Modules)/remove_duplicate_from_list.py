# Write a Python program to remove duplicates from a list.

mylist = [10,20,30,10,40,10,50,70,20]


# first we converted the list to set so the duplicate items will be removed
# then we converted set to the list 
print(list(set(mylist)))
