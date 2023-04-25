'''Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string: 'w3resource'
Expected output:
{'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}'''

# create a string
string = "w3resource"
# create an empty dictionary for further use
my_dict = {}

# using for loop to go through each letter of string
for i in string:
    # counting the letter repeatation
    if i in my_dict:
        my_dict[i]+=1
    else:
        my_dict[i]=1

# printing the dictionary
print(my_dict)