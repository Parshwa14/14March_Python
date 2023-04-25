'''Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,'d':400}
Sample output: Counter ({'a': 400, 'b': 400,'d': 400, 'c': 300}).'''

# importing the Counter method from the collections module
from collections import Counter

# creating two dictionaries
d1 = {'a': 100, 'b': 200, 'c' : 300}
d2 = {'a': 300, 'b': 200, 'd' : 400}

# creating a new variable result and using Counter method with both the dictionaries and adding them
result = Counter(d1) + Counter(d2)

# printing the final result
print(result)
