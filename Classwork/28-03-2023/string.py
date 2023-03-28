mystr = "hello this is python"


print(mystr)                # to print the whole string

print(mystr[0])             # to print the character at index : 0
print(mystr[1])             # to print the character at index : 1
print(mystr[-1])            # to print the character at index : -1

print(mystr[0:5])           # slicing of the string from index 0 to 4

print(len(mystr))           # to find the length of the string

print(mystr.strip())        # to remove the space from the start and the end

# # to capitalize the whole string (to get all the characters of the string in upper case)

print(mystr.upper()) 


# # to decapitalize the whole string (to get all the characters of the string in lower case)

print(mystr.lower())


# to replace the word in the string

print(mystr.replace("hello","hola!"))


# to make the first character of the string in upper case

print(mystr.capitalize())


# to make the last word character in lower case

print(mystr.casefold()) 


# to count how many times the characters is repeating

print(mystr.count("h"))


# to check if the string starts with the character

print(mystr.startswith("h"))



# to check if the string starts with the character

print(mystr.endswith("n"))


# to find the index value of the character is entered

print(mystr.index("i"))


# to check if the string is alphabet

print(mystr.isalpha())



# to check if the string is digits

print(mystr.isdigit())


# to check if the string is alphanumeric (spaces are not allowed)

print(mystr.isalnum())


# to check if the whole string is in upper case

print(mystr.isupper())


# to check if the whole string is in lower case

print(mystr.islower()) 


# to make every word of the string in capital 

print(mystr.title())