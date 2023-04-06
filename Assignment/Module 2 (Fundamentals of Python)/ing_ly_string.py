'''Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead if the string length of the 
given string is less than 3, leave it unchanged.'''

# first of all we will take a string from user
str =  input("Enter a String : ")

# the length is less than three then we dont have to make any change
# using lenth function to check the length
if len(str)<3:
    print(str,"(Unchanged)")

#for the length is three or more than three
else:

    # checking if string ending with "ing" using endswith function
    if str.endswith("ing"):
        #adding "ly" at the end of the string
        print(str + "ly")
    
    # this block is for string does not ends with ing 
    else:
        # add ing at the end of the string
        print(str + "ing")