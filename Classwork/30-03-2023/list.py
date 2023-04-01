food_list=["Burger","Sandwich","Pizza","Hotdog","Dhosa","Pav Bhaji"]

print(food_list)

# to print the value by its index
# print(food_list[0])
# print(food_list[2])

# slicing of the list (start:end)
# print(food_list[0:3])
# print(food_list[3:])
# print(food_list[-1])
# print(len(food_list))

# to print the items of the list in different(new) line
'''for items in food_list:
    print(items)'''

# to get the index of the element of the list
# print(food_list.index("Pizza"))

# to add an element to the list
# food_list.append("PaniPuri")

# to insert add an element to the list at a particular index
# food_list.insert(2,"Samsosa")

# to remove particular element from the list
# food_list.remove("Dhosa")

# to remove the last element of the list
# food_list.pop()

# to remove an particular element of the list by its index
# food_list.pop(3)

# to reverse the list (i.e [1,2,3,4,5]-> [5,4,3,2,1])
# food_list.reverse()

# to sort the list elements in ascending order
# food_list.sort()

# to delete all the elements of the list
# food_list.clear()

# to delete the whole list
# del food_list
# print(food_list)

restaurant_list=["Pizza Hut","McDonalds","Taj","Burger King","Subway"]

# to add lists (a+b)
# print(restaurant_list + food_list)

# to merge lists (add one list in to second list(a=(a+b)))
restaurant_list.extend(food_list)
print(restaurant_list)
