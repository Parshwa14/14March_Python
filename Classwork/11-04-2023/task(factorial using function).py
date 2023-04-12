def fact():
    n = int(input("Enter Number to find its Factorial : "))
    result = 1

    for i in range(1,n+1):
        result *= i
    
    print(f"The Factorial of [{n}] is [{result}]")


fact()