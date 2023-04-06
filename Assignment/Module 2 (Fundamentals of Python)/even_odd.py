# asking user to enter a number
n = int(input("Enter a Number : "))

#we will use if else to determine whether it is even or odd

# condition for even number (if n is divisble by 2 without any remainder)
if n%2==0:
    print("The Number is Even")

# when condition in if statement is false then it'll come to else part and that means it is odd number
else:
    print("The Number is Odd")
