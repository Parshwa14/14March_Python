#QUE : Write a program to check that you are eligible for licence or not.

age = int(input("Enter your Age : "))       #taking user input for age

if age>=18:                                 #condition to follow 
    print(f"You are {age} years old, You are eligible for Licence.")
else:
    print(" You are Under Age, You can apply for licence after",18-age,"years")