dataset = [10,56,31,78,99,34,32,90,12,3]

def multipleof3(i):
    if i%3==0:
        return True
    else:
        return False

filtered_num = filter(multipleof3,dataset)

for j in filtered_num:
    print(j)