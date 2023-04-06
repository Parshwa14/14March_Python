# taking a string from user
str = input("Enter a string: ")
# taking a substring from user
substr = input("Enter a substring to count: ")

# counting how many times the substring repeats in the string
count = str.count(substr)

# printing the conclusion about how many times substring occurs
print(f"The substring [{substr}] occurs [{count}] times in the string.")
