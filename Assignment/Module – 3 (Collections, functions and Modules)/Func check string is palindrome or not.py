# Write a Python function that checks whether a passed string is palindrome or not.

# taking a string from user
mystring = str(input("Enter a String : "))

# creating a function with parameter for palindrome
def palindrome(str):
    # converting the string in lower case
    string1 = mystring.casefold()
    # reversing the string
    string2 = string1[::-1]

    # using for loop to compare the string
    for i in string1:
        for j in string2:
            # comparing each letter of string
            if i==j:
                pal = True
            else:
                pal = False

    # for the condition is True string is palindromme
    if pal==True:
        print("The String is Palindrome")
    # for the condition is False string is not palindromme
    elif pal== False:
        print("The String is not Palindrome")


# calling the function with argument
palindrome(mystring)