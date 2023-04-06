# taking input of a letter from user
letter = input("Enter a Letter : ")

# converting it into small letters if there is a capital letter
vowel = letter.lower()


# using if else statement with or operator to find out if it's vowel or not 
if vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u":
    print(f"[{vowel}] is a Vowel")
    
else:
    print(f"[{vowel}] is not a Vowel")
