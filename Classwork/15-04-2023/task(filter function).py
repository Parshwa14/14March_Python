dataset = [10,56,31,78,99,34,32,90,12,3]

def even(i):
    if i%2==0:
        return True
    else: 
        return False
    
filtered_num = filter(even,dataset)

for j in filtered_num:
    print(j)

