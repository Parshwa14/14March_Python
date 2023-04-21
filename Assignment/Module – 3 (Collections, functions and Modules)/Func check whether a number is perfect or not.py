# Write a Python function to check whether a number is perfect or not.

# defining a function
def perf_num(num):

    # the number is zero or less than zero than it is not perfect number
    if num<=0:
        return False
    
    # to satisfy the condition of perfect number add the factors of the number
    # initializing the factorial_sum as 0 for further use
    factor_sum = 0

    # using for loop to check each number from 1 to num
    for i in range(1,num):
        # num is divided by i with remainder as 0 then i will be added to factorial_sum
        if num%i==0:
            factor_sum+=i 
            
            # final value of factorial_sum and num are same than the number is perfect number and return True
            if factor_sum == num:
                return True
    return False
        

print(perf_num(5))
print(perf_num(6))
print(perf_num(28))
print(perf_num(496))
print(perf_num(10))
print(perf_num(15))
