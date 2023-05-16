# Que : Write a python program to find the longest words.

# getting input from the user
text = input("Enter A Sentance : ")

# split the text into individual words
words = text.split()

# creating an empty list
long_word = []

# creating a variable for max length
max_len = 0

# using for loop to go through each word
for word in words:
    # getting the word length 
    word_len = len(word)
    
    # comparing the word lenght to the max length
    if word_len > max_len:
        # if word length is more than max length then the new max length will be the word length
        max_len = word_len
        # and add the word of max length to the list
        long_word = [word]
    
    # elif for if there will be any word with the same length as the max lenght then
    elif word_len == max_len:
        # it will append the word to the long word list
        long_word.append(word)

# if the list long word is not empty then using for loop print the elements one by one
if len(long_word)>0:
    print("Longest Word : ")
    for i in long_word:
        print(i)

# there is no elements in the list long word then print the message below
else:
    print("No Longest word found...")

