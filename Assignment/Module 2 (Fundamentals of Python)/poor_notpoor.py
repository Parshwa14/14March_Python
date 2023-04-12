'''Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given 
string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring  with 'good'. 
Return the resulting string.  '''

#taking an input of string from user
mystr = input("Enter a String : ")        

# finding the substring 'not' in the string 
str_not = mystr.find('not')

# finding the substring 'poor' in the string 
str_poor = mystr.find('poor')

#conditions for detecting that substrings are next to each other like this 'not poor'
if str_poor > str_not and str_not>0 and str_poor>0:
  
  #replacing not poor with good
  mystr = mystr.replace(mystr[str_not:(str_poor+4)], 'good')
  print(mystr)

else:

  # when the substrings are not next to each other we will return the string unchanged
  print(mystr)
