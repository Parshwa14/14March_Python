# Write a Python function to insert a string in the middle of a string.

# defining a function 
def addstr():

# creating two string variables 
    mystr = "Hello This is a Operation"
    midstr = "string"

# adding the midstr to the mystr with the help of slicing
    newstr = mystr[:16] + midstr + mystr[9:]

# returning the newstr(resulting string)
    return newstr

# storing the function to variable called x to call easily and it looks clean
x = addstr()

# calling and printing the function by the help of variable x 
print(x)