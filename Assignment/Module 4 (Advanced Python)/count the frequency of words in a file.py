# Que : Write a Python program to count the frequency of words in a file.

# creating an empty dictionary for the word frequency
word_frequency = {}

# opening the file in read mode
file = open("how to define a python class.txt",'r')

# going through each line in the file
for line in file:
    
    # splitting the words from every line
    word = line.split()
    
    # using the lower method to lower all the words for handling the program with ease
    for i in word:
        i = i.lower()
        
        # the word is already in the dictionary then this will increase its frequency
        if i in word_frequency :
            word_frequency[i] += 1
        # the word is not in the dictionary then this will add it to the dictionary
        else:
            word_frequency[i] = 1
            
# if the length of the dictionary word frequency is more than 0 then it will print the results
if len(word_frequency)>0:
    print("Word Frequency : ")
    for x,y in word_frequency.items():
        print(f"{x} = {y}")

# if the length of the dictionary word frequency is 0 then it will print the message below
else:
    print("No Words Found...")