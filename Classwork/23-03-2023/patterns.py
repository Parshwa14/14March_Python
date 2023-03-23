#nested for loop
'''
for r in range(6):
    for c in range(6):
        print("*",end=" ")
    print(" ")

#square pattern
       
'''

#right angle triangle pattern

# for r in range(6):                              
#     for c in range(r):
#         print("*",end=" ")
#     print(" ")


# for r in range(6):
#     for c in range(r):
#         print(c+1,end=" ")
#     print(" ")

for r in range(6,0,-1):                  #iteration started from 6 and decreases with 1 till 0                 
    for c in range(r):               #in first row the iteration will go till 0 to (r-1)=5 and so on...
        print("*",end=" ")
    print(" ")
