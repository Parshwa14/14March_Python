#QUE : Python Program to check if the given year is leap year or not.

year = int(input("Enter a Year :"))

if year%4==0:
    print(f"{year} is a Leap Year")

else:
    print(f"{year} is not a Leap Year")