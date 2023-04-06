# taking two number from user
a = int(input("Enter number A : "))
b = int(input("Enter number B : "))


# printing A and B before swap

print("______________________")
print("Before Swap")
print(f"A = {a}, B = {b}")     

(a,b) = (b,a)                   # swapping numbers without temp variable


# printing A and B after swap
print("______________________")
print("After Swap")
print(f"A = {a}, B = {b}")
