import keyword

keyword_list = keyword.kwlist

# to get the list of the keywords
print(keyword_list)

# to check if a word is keyword or not
word = input("Enter a word : ")
if word in keyword_list:
    print("It is a Keyword")
else:
    print("It is not a Keyword")
    