'''# normal function with normal parameter

def sum(a,b):
    ans = a+b
    print(ans)

sum(10,20)

'''


'''# args function

def addition(*n):
    ans = 0
    for i in n:
        ans+=i
        print(ans)

addition(10,20,30,40,50,60,70,80,90,100,110,120,130,140)


'''



# kwargs 

def myfun(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} = {v}")


myfun(name = "Parshwa", subject = "Python", City = "Gandhinagar")