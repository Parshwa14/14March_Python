"""
Exception : whic disturbs normal flow of program.

            It can be handled by try and except block
            and this process is known as Exception Handling
            
            Exception coding will be done by developer side 
            
syntax : 
        
            
        try:
            exception code
        except:
            statement
            
"""

# normal code without exception 
# print(a)

# code with exception

'''try:
    print(a)

except:
    print("Invalid Input!!!")

'''

'''
try: 
    num1=int(input("Enter number 1 : "))
    num2=int(input("Enter number 2 : "))

    ans = num1/num2
    print(ans)
except:
    print("Cannot Divide by Zero")
    '''


try:
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))

    ans = num1/num2
    print(ans)

except ValueError:
    print("Only Integers Allowed")

except ZeroDivisionError:
    print("Cannot Divide by Zero!")