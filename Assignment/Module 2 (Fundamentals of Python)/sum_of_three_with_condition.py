# WAP to sum of three given integers.However,if two values are equal sum will be zero.
a = int(input("Enter A : "))
b = int(input("Enter B : "))
c = int(input("Enter C : "))

# using if else and operator to check if any two values are same 
#if any of two values are same the sum will be zero

if a==b or b==c or a==c:
    print("The Sum is : 0 ")

# if there is all the values are different it will add the three
else:
    print("The Sum is :",a+b+c)