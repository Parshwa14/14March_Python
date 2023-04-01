mylist=[]               #creating an empty list

# taking the input from user of how many elements user wants
n=int(input("Enter the number of elements :- "))            

# using for loop to take take value from user one by one n times 
for items in range(n):

    #taking input from user for elements
    el=input("Enter your elements :- ")             

    # adding the input entered by user to the empty list we have created
    mylist.append(el)                               

# printing the list after adding the elements to it 
# writing it outside the for loop to get the right output
print(mylist)