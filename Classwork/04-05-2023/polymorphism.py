"""
polymorphism: Poly means many and morphism means forms. So polymorphism means many forms.

1) Method Overloading : Python does not supports method overloading.

2) Method Overriding : When two class have same method name is called method overriding.

"""


class animal:
    def walk(self):
        print("Animal Walking")

class dog(animal):
    def walk(self):
        print("dog walking")
    

d = dog()
d.walk()

a=animal()
a.walk()