myset = {"A", "B", "C", "D","E", "A", "B", "F"}

'''# to print the elements of the set
print(myset)

# to find the length of the set
print(len(myset))

# to find if the particular element is in the set 
if "F" in myset:
    print("YESSSS.....")
else:
    print("NO.....")

# for printing the elements of the set in different line
for items in myset:
    print(items)


# to add an item in set
myset.add("P")
print(myset)

# to add more than one item in set
myset.update(["X", "Y", "Z"])
print(myset)


# to remove an item from the set
myset.remove("A")
print(myset)
    

# to remove the last item of the set
myset.pop()
print(myset)

# to delete the set
del myset 

print(myset)
'''
newset={"P", "Q", "R", "S", "T", "A", "B"}
# print(newset)
# print(myset)
# merge values of the two sets
# x = newset.union(myset)
# print(x)


# get the common values of the two sets
x = newset.intersection(myset)
print(x)


