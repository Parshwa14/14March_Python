'''Write a Python program to combine values in python list of dictionaries. 
Sample data:[{'item': 'item1', 'amount': 400},{'item': 'item2', 'amount':300},{'item': 'item1', 'amount': 750}]
Expected Output:
Counter ({'item1': 1150, 'item2': 300})'''

# importing counter from collections module
from collections import Counter

# creating a list of dictionaries
my_dict = [{'item': 'item1', 'amount': 400},{'item': 'item2', 'amount':300},{'item': 'item1', 'amount': 750}]

# creating a variable result storing Counter() method in it
result = Counter()

# the using for loop to go through each dictionary in the list
for i in my_dict:
    # add the value of items and amount and storing in result
    result[i["item"]] += i["amount"]

# print result for final output
print(result)