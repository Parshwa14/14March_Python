mydict={}

n=int(input("Enter the number of pairs you want:"))

for i in range(n):
    key = input("Enter Key : ")
    value =input("Enter value : ")
    mydict[key]=value

print(mydict)