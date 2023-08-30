class Animal(object):
    def __init__(self, name):
        self.name=name
        print("Passing init in Animal Class")

class Dog(Animal):
    def __init__(self, name, breed):
        print("Passing init in Dog class for 1st time")
        super().__init__(name)
        print("Passing init in Dog class for 2nd time")
        self.breed=breed
        print("The breed of %s is %s" %(self.name, self.breed))

dg=Dog("Tommy", "pug")



