# Write python program that user to enter only odd numbers, else will raise an exception.
import sys

try : 
    num=int(input("Enter Odd number:"))
    if num%2==0:
        raise ValueError("Even Number Entered!!")
except:
    print("subject= ",sys.exc_info()[0])
    print("message= ",sys.exc_info()[1])
