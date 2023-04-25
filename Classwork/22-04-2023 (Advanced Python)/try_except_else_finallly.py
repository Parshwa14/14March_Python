''' 
try:
    exception code
except:
    after exception statement
else:
    without exception
finally:
    it always occur
'''


'''
try:
    a=10
    b=20
except:
    print("Invalid Input!")

else:
    print("Welcome to Math World")

finally:
    print("Thank You For Using Our Application")'''


'''
l1 = [10,120,540,50,67,32,756,64,3,21]

try:
    print(l1[5])
except:
    print("Index out of Range")
else:
    print(l1)'''

try:
    print(10/0)

except Exception as e:
    print(e)