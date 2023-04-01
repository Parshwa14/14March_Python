# taking the number of how many elemets we want
n=int(input("Enter Number of elements you want "))

# creating an empty list
newlist=[]

# using for loop to get input n(the number we entered) times
for i in range(n):
    item = input("enter element : ")
    newlist.append(item)

'''converting the list into set and then the duplicate items will be removed and
   then converting the set into list again
'''
print(list(set(newlist)))           

