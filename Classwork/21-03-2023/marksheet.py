s1=int(input("Enter the marks of subject 1 : "))
s2=int(input("Enter the marks of subject 2 : "))
s3=int(input("Enter the marks of subject 3 : "))
s4=int(input("Enter the marks of subject 4 : "))

if s1>=35 and s2>=35 and s3>=35 and s4>=35:
    total = s1+s2+s3+s4
    print("Total",total)

    per=total/4
    print("Percentage",per)

    if per>=70:
        print("Result : Distinction")
    elif per>=60:
        print("Result : First Class")
    elif per>=50:
        print("Result : Second Class")
    elif per>=40:
        print("Result : Pass Class")
else:
    print("Fail")