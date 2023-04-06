'''Write a Python program to get a single string from two given strings, separated by a space 
and swap the first two characters of each string.  '''


# first we will take two strings from user
str1 = input("Enter String 1 : ")
str2 = input("Enter String 2 : ")

# swap first two characters of the strings
new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]

# combining the strings after swapping separated by a space
final_str = new_str1 + " " + new_str2

#printing the final string
print(final_str)