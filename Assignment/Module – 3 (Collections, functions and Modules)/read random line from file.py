# Write a Python program to read a random line from a file.

# importing random module
import random

# using append mode to create and append the lines to the file
f = open("file.txt","a")
 # writing to the file
f.write("But I must explain to you how all this mistaken idea of denouncing pleasure and \npraising pain was born and I will give you a complete account of the system, \nand expound the actual teachings of the great explorer of the truth, the \nmaster-builder of human happiness. No one rejects, dislikes, or avoids \npleasure itself, because it is pleasure, but because those who do not know how \nto pursue pleasure rationally encounter consequences that are extremely painful.\nNor again is there anyone who loves or pursues or desires to obtain pain of itself, \nbecause it is pain, but because occasionally circumstances occur in which toil and \npain can procure him some great pleasure. To take a trivial example, which of us \never undertakes laborious physical exercise, except to obtain some advantage from it? \nBut who has any right to find fault with a man who chooses to enjoy a pleasure that \nhas no annoying consequences, or one who avoids a pain that produces no resultant pleasure?")

# reading the file
f= open("file.txt","r")

# using readlines function 
readd = f.readlines()

# using random and choice function from the random module to get a random line
readrandom = random.choice(readd)

# printing the random line
print(readrandom)

# closing the file
f.close()