'''Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
If the string length is less than 2, return instead of the empty string.  '''

# first of all taking a string from user
str = input("Enter a String : ")

# checking for the length of the string
if len(str)>2:
    # the length of string is more than two
    # the new string will be combination of the first and last two characters of the string
    n_str = str[:2] + str[-2:] 
    print(n_str)
else:
    #the string length is 2 or less than 2 then return empty string
    print("")
