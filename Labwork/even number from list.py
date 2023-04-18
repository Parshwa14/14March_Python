# Write a Python program to print the even numbers from a given list

# creating a list
mylist = [12,13,51,64,19,21,94]

print("Even Numbers : ")

# using for loop to iterate each element of list
for i in mylist:
    # using conditional statement to find the even number
    if i%2==0:
        # printing the number and used end="  " to print the numbers in a single line
        print(i,end="  ")