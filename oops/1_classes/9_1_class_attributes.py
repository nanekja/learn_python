class MyClass(object):
    classy=10 #class attribute

    def set_val(self):
        self.insty=100 #instance attribute

obj1=MyClass()

obj1.set_val()

print(obj1.classy) # we can call class attribute
print(obj1.insty)  # we can also call instance attribute

