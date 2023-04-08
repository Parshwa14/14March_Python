start = 2
end = 30
print("Prime numbers between : ",start,"and",end,"are : ")

for num in range(start,end):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break

        else: 
            print(num)