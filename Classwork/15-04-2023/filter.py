"""
filter() : It is a method which can filter the given sequence with the help of function that 
test each element of the sequence.


syntax : 
    
        filter(func,sequence)
"""

'''# check vowel normally without filter

l1 = ["a","e","v","z","x","t","o"]

vowel_list = ["a","e","i","o","u"]
l2=[]

def checkvowel():
    for c in l1:
        if c in vowel_list:
            l2.append(c)
        
checkvowel()
print(l2)'''


# check vowel using filter


l1 = ["a","f","h","k","i","o"]
vowel_list = ["a","e","i","o","u"]

def myfunc(seq):
    if (seq in vowel_list):
        return True
    else:
        return False

filtered_data = filter(myfunc,l1)

for i in filtered_data:
    print(i)