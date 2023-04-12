# Write a Python function to reverses a string if its length is a multiple of 4.

# creating a function with parameter mystr
def reverstring(mystr):

# using if else statement and operator to fulfil the condition(length is multiple of 4)
    if len(mystr)%4==0:

# reversing the string by slicing and then printing it        
        revstr = mystr[::-1]
        print("Reversed : ",revstr)

# in else part the string will be unchanged
    else:
        print("Unchanged : ",mystr)


reverstring("four")
reverstring("elements")
reverstring("checkmate")