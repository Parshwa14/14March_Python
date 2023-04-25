import sys
try:
    print(a)
except:
    print("subject= ",sys.exc_info()[0])
    print("message= ",sys.exc_info()[1])
    