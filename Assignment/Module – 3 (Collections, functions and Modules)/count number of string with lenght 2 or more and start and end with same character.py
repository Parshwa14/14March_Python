'''Write a Python program to count the number of strings where the string length is 2 or more 
and the first and last character are same from a given list of strings.'''

# creating a list of strings
list_string = ["saas","yaay","sap","rat","loop","noon","SOS","zoo"]

# creating a variable count initializing it with 0
count = 0

# using for loop to go through each item of list
for s in list_string:
    
    #using condtional statement and operator check if the condition satsifies
    if len(s)>=2 and s[0]==s[-1]:

        # increasing by 1 if the condition is satifies
        count +=1

# printing the count
print(count)