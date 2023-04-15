# Write a Python function that takes two lists and returns true if they have at least one common member.

# defining a function
def commonmem():

    # creating two empty lists
    list1=[]
    list2=[]

    # taking two varaibles for number of list elements
    # then using for loop and append method to add to list
    n1 = int(input("Enter no. of elements for list 1 : "))
    print("List 1")
    for i in range(n1):
        el1=input("Enter element :")        #taking element from user
        list1.append(el1)                   #appending the element to the list
    
    n2 = int(input("Enter no. of elements for list 2 : "))
    print("List 2")
    for j in range(n2):
        el2=input("Enter element :")        #taking element from user
        list2.append(el2)                   #appending the element to the list

#printing the both lists
    print("List 1\n",list1,"\nList 2\n",list2)
    # using nested loop for checking each element from both the list
    for i in list1:
        for j in list2:
            
            # conditional statement for common element to return True
            if i==j:
                return True
            

# calling and printing function by storing it in a variable 
x = commonmem()
print(x)
    
       
