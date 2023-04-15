print("\n\t\t\t||| Infinite Addition Program |||")
print("\t\t\t_________________________________\n")
print("""\t\t\tInstructions :\n
\t\t\t1) Enter as Many Numbers you want
\t\t\t2) Enter 0 as a last number to end the Addition program 
""")
print("__________________________________________________________________________________________________")

# taking a variable for addition,count and number
add = 0
count = 0
num = ""

# using while loop 
# when num==0 the loop will stop
while num!=0:
    num=int(input("Enter number : "))
    # adding the number to addition variable
    add+=num
    # adding 1 to count each time the loop runs
    count +=1

print("Total Numbers = ",count-1)
print("Addition = ",add)