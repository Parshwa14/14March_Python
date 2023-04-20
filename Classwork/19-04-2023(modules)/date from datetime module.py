# importing the date function from the module datetime
from datetime import date

'''# creating a variable named my date for today's date
mydate =  date(2023,4,19)

# printing today's date 
print(mydate)
'''
# now we are fetching the date from the module datetime
current_date = date.today()
print(current_date)

# for printing the day month and year separately 
print(current_date.year)
print(current_date.month)
print(current_date.day)