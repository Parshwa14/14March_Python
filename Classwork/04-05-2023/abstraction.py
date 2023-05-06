"""
Abstraction: Abstraction is used to handle the complexity of program by hidin the unneccessary information from the user.

For Abstraction we have to import ABC class and abstractclassmethod

ABC - Abstract Base Class

Abstraction is used for hiding the background information of the code

"""

from abc import ABC, abstractclassmethod
class RBI(ABC):
    def roi(self):
        pass
class SBI(RBI):
    def roi(self):
        return 8.5

class BOI(RBI):
    def roi(self):
        return 6.5    
sbi=SBI()
print(sbi.roi())

boi=BOI()
print(boi.roi())
