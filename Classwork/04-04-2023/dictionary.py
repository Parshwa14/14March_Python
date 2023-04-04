stdata = {"id":1, "name":"Parshwa", "sub":"python"}             #dictionary

'''print(stdata)                                   # print the dictionary
print(stdata["name"])                           # to print the value from key

print(stdata.get("sub"))                        # other method to get the value from key
print(len(stdata))                              # to get the length of dictionary

print(stdata.keys())                            # to get all the keys 

print(stdata.values())                          # to get all the values

'''

# the output will be no because it will get confused whether to check in keys or values
'''
if "Parshwa" in stdata:
    print("Yess...")                            
else:
    print("No..")'''
'''
# it will check specifically in values 

if "Parshwa" in stdata.values():
    print("yess..")
else:
    print("no...")'''

'''
for i in stdata:            # to get the keys with help of for loop
    print(i)'''

'''
for i in stdata.values():    # to get the values with help of for loop
    print(i)'''


'''
for i in stdata.items():     # to get key-values with help of for loop
    print(i)'''

# key = id and value = 1
# key = name and value = Parshwa
# key = sub and value = python
'''
for i,j in stdata.items():
    print(f"key = {i} and value = {j}")'''


# to add new data
'''
stdata["city"] = "Ahmedabad"
print(stdata)'''


# to remove data from dictionary
'''stdata.pop("sub")
print(stdata)'''


# to clear the dictionary
'''
stdata.clear()
print(stdata)'''

# to delete the dictionary
'''
del stdata
print(stdata)'''



''' newdict=stdata.copy()     # to copy dictionary to another dictionary
print(newdict)'''