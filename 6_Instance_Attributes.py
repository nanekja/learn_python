# We have seen that an instance can access variables defined in the class
# Here we will set the value of an attribute not in the class but in the instance itself.
# This is the data that we were talking about when we said that an object is a unit of data.
# Instance values are stored right in the instance using the instances attributes

import random

class MyClass(object):
    def mymethod(self):
        self.val = random.randint(1,10)

myinst=MyClass()
myinst.mymethod()

print(myinst.val)

# We call the attributes of an instance the State of the instance.
