# Write a Python program to count the occurrences of each word in a given sentence  

# input of sentance from user
sentence = input("Enter a sentence: ")
#splitting and decapitilizing the words from the sentance
words = sentence.split().lower()

#creating an empty dictionary to store word and frequency
frequency = {}

#using for loop to count each word from the words
for word in words:
    #if the words repeats more than one time frequency will be added by one everytime
    if word in frequency:
        frequency[word] += 1
    #else it will be stored as one
    else:
        frequency[word] = 1

print("Word Frequency")
#printing the word and frequency that is stored in the empty dictionary we have created
for word, count in frequency.items():
    print(f"{word}: {count}")
