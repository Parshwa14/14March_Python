# Write a Python function that takes a list and returns a new list with unique elements of the first list.

# first taking number of list elements user wants to add in the list
n = int(input("Enter number of element you want in list : "))

# taking an empty main list
l1=[]
# taking an empty unique list
unq_list=[]

# taking input from user for list elements
for i in range(n):
    el = input("Enter Element : ")
    # appending the elements to the list
    l1.append(el)

# checking if the list element if repeating 
for j in l1:
    # if the number is unique the append it to the unique list
    if j not in  unq_list:
        unq_list.append(j)

# printing both the lists
print("Main List\n",l1)
print("Unique List\n",unq_list)