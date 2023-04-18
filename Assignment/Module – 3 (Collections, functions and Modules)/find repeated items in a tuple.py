# Write a Python program to find the repeated items of a tuple.

# creating a tuple
mytuple = (1,2,3,1,2,4,5,6,7,7,7,8,)
# creating an empty list for adding repeated items
repeat = []

# using for loop to go through each item of tuple
for i in mytuple:
    
    # using conditional statement and methods and operators to find repeated items
    if mytuple.count(i)>1 and i not in repeat:
        
        # appending the repeated item to the empty list
        repeat.append(i)

# printing the repeated item list
print("The Repeated Items are : ",repeat)
