number=int(input("Enter a Number : "))

if number%5==0 and number%11==0:
    print(f"{number} is divisible with 5 and 11")
else:
    print(f"{number} is not divisible with 5 and 11")