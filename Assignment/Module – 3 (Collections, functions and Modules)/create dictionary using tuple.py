# How will you create a dictionary using tuples in python?

# method 1 using list of tuples

mylist =[("one",1),("two",2),("three",3)]
mydict = dict(mylist)
print(mydict)

# method 2 using tuple of tuples
mytuple = (("five",5),("six",6),("seven",7))
mydictionary = {key:value for key, value in mytuple}
print(mydictionary)
