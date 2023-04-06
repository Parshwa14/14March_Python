# Write a Python program to count the number of characters (character frequency) in a string  

# taking an input of string from user
str1 = input("Enter a string : ")

# removing all the spaces if there is any
# converting the string into lower because it will iterate differently for capital letters
str2=str1.replace(" ","").lower()

#creating an empty dictionary for further use
freq ={}

# using for loop to iterate one by one character from the entered string
for char in str2:
    # if there is repeating character it will add 1 in frequency everytime it repeats
    if char in freq:
        freq[char]+=1
    #if the character is in the string only one time then frequency will be one
    else:
        freq[char]=1

print("character frequency")
for char,count in freq.items():
#printing the character frequency character:how many times it repeats
    print(f"{char}:{count}")
