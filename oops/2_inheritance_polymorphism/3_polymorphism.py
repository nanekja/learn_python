class Animal(object):
    def __init__(self,name):
        self.name=name

    def eat(self,food):
        print("%s eats %s" %(self.name,food))

class Dog(Animal):
    def fetch(self, thing):
        print("%s fetches %s" %(self.name, thing))

    def show_affection(self):
        print("%s wags tail" %(self.name))

class Cat(Animal):
    def swatstring(self):
        print("%s shreds the string" %(self.name))

    def show_affection(self):
        print("%s purrs" %(self.name))

dg=Dog("Tommy")
ct=Cat("Pilli")

# Here the methods are different but conceptually similar. This allows for expressiveness in design. A group of related classes implement same action
dg.show_affection()
ct.show_affection()

