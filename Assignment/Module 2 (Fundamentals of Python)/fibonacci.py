# Write a Python program to get the Fibonacci series of given range.

n=int(input("Enter a Number : "))
n1=0
n2=1

# if user enters 0 as input
if n==0:
    print("Invalid Input!!!")

# if user enters 1 as input
elif n==1:
    print("Fibonacci Sequence :",n1)

# if user enters 2 as input
elif n==2:
    print("Fibonacci Sequence :",n1,n2)    

# if user enters n>2 as input
else:
    print("Fibonacci Sequence :",n1,n2,end=" ")         

    for i in range(2,n):

        # it will get 3rd number from n1 and n2 as they are already delcared
        n3=n1+n2                                        

        # new n1 is the old n2
        n1=n2                                           

        # new n2 is the n3
        n2=n3

        #it will print every time the loop runs
        print(n3,end=" ")           #it will print in the same line but after a space as we used end