"""
Inheritance : When one class inherits from another class is called Inheritance.

Parent class : Base class/ Super class
Child class : Derived class/ Sub class

-> child class can access all the properties of parent class.

Types of Inheritance : 

1) Single Level Inheritance:

        class A
            |
            |
            |
        class B


2) Multilevel Inheritance:

        class A
            |
            |
        class B
            |
            |
        class C


3) multiple Inheritance: In multiple Inheritance we can inherit multiple child class from parent class

        class A         class B
            \               /
             \             /
              \           /
               \         /
                \       /
                 \     /
                  \   /
                 class C

                 
4) Hierarchical Inheritance: When more than one derived class created from single base class is called Hierarchical Inheritance.

        class A
           / \             
          /   \           
         /     \         
        /       \       
       /         \     
      /           \   
   class B      class C


5) Hybrid Inheritance : It is a combination of different Inheritance


"""




'''
# single level inheritance
class parent:

    def house(self):
        print("3 BHK House")


class child(parent):

    def car(self):
        print("Mercedes Car")



c = child()

c.house()
c.car()'''



'''
# multilevel inheritance

class Grandparent:

    def land(self):
        print("30 Acres of Land")

class parent(Grandparent):

    def house(self):
        print("5 BHK House")


class child(parent):

    def car(self):
        print("Audi Car")



c = child()

c.land()
c.house()
c.car()'''


'''
# multilevel Inheritance

class Calculation:

    def summation(self,a,b):
        return a+b
    

class Calculation2:
    def multiplication(self,a,b):
        return a*b
    

class Derived(Calculation,Calculation2):

    def divide(self,a,b):
        return a/b
    

d = Derived()

print("Sum is : ",d.summation(1,5))
print("Multiplication is : ",d.multiplication(5,5))
print("Division is : ", d.divide(10,2))'''


'''
# hierarchical Inheritance

class parent:
    def func1(self):
        print("This Function is in Parent class")


class child1(parent):
    def func2(self):
        print("This function is in child 1")
    
class child2(parent):
    def func3(self):
        print("This function is in child 2")
    


c1 = child1()
c2 = child2()

print("child class 1")
c1.func1()
c1.func2()

print("\nchild class 2")
c2.func1()
c2.func3()
'''



# Hybrid Inheritance
class greatgrandparent:
    def village(self):
        print("Haveli in Village")

class grandparent(greatgrandparent):
    def land(self):
        print("100 Acres Land")

class father(grandparent):
    def house(self):
        print("5 BHK House")
    
class mother(grandparent):
    def house2(self):
        print("Villaa")
    

class child1(father,mother):
    def car(self):
        print("Jaguar Car")

class  child2(father,mother):
    def bike(self):
        print("Kawasaki Z900")


class grandchild(child1,child2):
    def smartphone(self):
        print("Iphone 20 pro max Ultraaa")

    


gc = grandchild()
gc.village()
gc.land()
gc.house()
gc.house2()
gc.car()
gc.bike()
gc.smartphone()