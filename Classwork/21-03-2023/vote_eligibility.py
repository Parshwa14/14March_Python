name=input("Enter Your Name : ")
age=int(input("Enter Your age : "))

if age>=18:
    print("You can Vote!")

elif age<18:
    print("You can Vote after " ,18-age,"years")

else:
    print("Invalid Input...")