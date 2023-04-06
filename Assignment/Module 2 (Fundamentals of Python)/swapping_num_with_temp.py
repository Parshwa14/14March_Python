# taking two number from user
a = int(input("Enter number A : "))
b = int(input("Enter number B : "))


# taking a variable temp for swapping
temp = ""


# printing A and B before swap

print("______________________")
print("Before Swap")
print(f"A = {a}, B = {b}")     


# logic for swapping using temp variable

temp = a
a=b
b=temp


# printing A and B after swap

print("______________________")
print("After Swap")
print(f"A = {a}, B = {b}")
