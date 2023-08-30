class Animal(object):
    def __init__(self, name):
        self.name=name

    def eat(self, food):
        print("The %s eats %s" %(self.name, food))

class Dog(Animal):
    def fetch(self, thing):
        print("The %s goes after %s" %(self.name, thing))

class Cat(Animal):
    def swatstring(self):
        print("The %s shreds the string" %(self.name))

dg=Dog("Tommy")
ct=Cat("Pilli")

dg.eat("dog biscuits")
ct.eat("cat food")

dg.fetch("bone")
ct.swatstring()



