"""

OOPS - object oriented programming structure/system

class - It is a blueprint of a object. In python we can declare class as class keyword.

object - It is a instance of a class.
ex.,
car - volvo,mercedes,ertiga
student - name,subject,marks,id



syntax:

                class classname:
                    statements

method : It is declared iniside the class
function : It is declared outside the class

self : This is used to define that object is of this class, We have to write self compulsory.

"""

class student:
    stid = 10
    stnm = "Parshwa"


    def getdata(self):
        print("This is the data of student")


#  object creation

st =student()
print(f"Student ID : {st.stid}" )
print("Student Name : ",st.stnm)
st.getdata()
