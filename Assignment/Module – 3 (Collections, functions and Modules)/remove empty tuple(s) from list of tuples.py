# Write a Python program to remove an empty tuple(s) from a list of tuples.


# create a list of tuples
mylist = [("Apple"),(),("two",3,4),("Ozone"),(),("Sunrays","Far"),("1000"),()]

# using for loop to go through each element 
for i in mylist:
    # length of element is 0 then remove it
    if len(i)==0:
        mylist.remove(i)

# print final list with no empty tuples
print(mylist)