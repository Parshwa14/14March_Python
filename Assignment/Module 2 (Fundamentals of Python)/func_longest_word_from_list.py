# Write a Python function that takes a list of words and returns the length of the longest one.

# defining a function named maxlen
def maxlen():

# creating a list words with 5 elements
    words=["one","two","three","four","five"]
    
# taking longest as 0 so we can use it as an standard to find the max
    longest=0

# using for loop to iterate each element from the list
    for i in words:

# if else statement to find the element having longest length
# comparing each element with the longest length which is 0
        if len(i)>longest:
        
# if length of i is greater than longest than we will store it to longest then iterate again and find the longest
            
            longest=len(i)

# once we get the longest element we print the element and its length
    print(f"Longest from list is [{i}] and its length is [{longest}]")

# calling the function
maxlen()
