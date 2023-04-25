'''Write a Python program to create and display all combinations of letters, selecting each letter 
from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}
Expected Output:
ac ad bc bd'''

# creating a dictionary
data = {'1': ['a','b'], '2': ['c','d']}

# creating two different list by the keys of the dictionary 
l1 = data["1"]
l2 = data["2"]

# using nested for loop and adding all the values the key have 
for i in l1:
    for j in l2:
        
        # printing the final output
        print(i+j,end=" ")
