mytup = ("Rajkot", "Ahmedabad", "Baroda", "Surat", "Gandhinagar")
'''
# to print the tuple
print(mytup)

# to print the specific element by the index
print(mytup[1])
print(mytup[-1])

# to print the more than one element from the tuple (slicing)
print(mytup[0:3])

# to find the length of the tuple
print(len(mytup))

# to find if the element is in the tuple
if "Ahmedabad" in mytup:
    print("Yessssssssssss....")

else:
    print("No.................")


# to print all the elements of the tuple line by line
for items in mytup:
    print(items)
    '''

# to find the index of the particular element of the tuple

print(mytup.index("Rajkot"))
print(mytup.index("Gandhinagar"))

# to delete the tuple
del mytup

print(mytup)