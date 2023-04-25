# Write a Python program to map two lists into a dictionary.

# creating two lists named key and value
key = ["mango", "guava", "peach"]
value = [2,5,10]

# creating an empty dictionary
mydict = {}

# mapping two lists in dictionary by using for loop
for i in range((len(key))):
    mydict[key[i]]=value[i]

# printing the dictionary
print(mydict)