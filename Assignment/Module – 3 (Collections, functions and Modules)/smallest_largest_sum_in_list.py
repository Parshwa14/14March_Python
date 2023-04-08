# Write a Python function to get the largest number, smallest num and sum of all from a list.

#creating an empty list
mylist=[]

#using the sum variable for storing the sum of all from the list
sum = 0 

# asking user for how many elements they want in the list 
n=int(input("Enter number of element of the list : "))

# using for loop to ask user to enter elements and append it to the list
for i in range(n):
    el=int(input("Enter Element of the list : "))
    mylist.append(el)

# displaying the list to the user
print(mylist)

# sorting the list to find the smallest and the largest number from the list
mylist.sort()

print("__________________________________________________")
# after sorting the first element of the list will be the smallest
print("The Smallest Number in the List is : ",mylist[0])

print("__________________________________________________")
# after sorting the last element of the list will be the largest
print("The Largest Number in the List is : ",mylist[-1])

print("__________________________________________________")

# using for loop to sum the elements of the list
for i in mylist:
    sum += i        #adding each element of the list in the sum variable 

print("The Sum of all the Elements of the list is : ",sum)