#QUE : Python Program to find maximum between the three numbers

# first we will take three numbers a,b,c from user 

a = int(input("Enter Number A : "))
b = int(input("Enter Number B : "))
c = int(input("Enter Number C : "))

# now the condition and logic for finding the max number among the three numbers

if a>b and a>c:
    print(f"A = {a} is Maximum Number among Three")
elif b>c:
    print(f"B = {b} is Maximum Number among Three")
elif c>b:
    print(f"C = {c} is Maximum Number among Three")

else:
    print("ALL ARE EQUAL")