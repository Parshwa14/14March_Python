# Write a Python function to check whether a number is in a given range

# defining a function with three parameters number start end
def range_check(number,start,end):

    # using conditional statement to verify 
    if start<= number <= end:
        print(True)
    else:
        print(False)

# calling the functions with arguments
range_check(3,0,10)
range_check(100,50,250)
range_check(-5,0,-10)