class MyClass(object):
    count=0 # class variable

    def __init__(self, value):
        self.val=value
        MyClass.count+=1  # here class variable is being referenced in obj.attribute notation as class is also an object for python
        # above we could have simply called the variable "count" instead of "MyClass.count" but this is to differentiate any global variables with class variables

    def set_val(self, newval):
        self.val=newval

    def get_val(self):
        return self.val

    def get_count(self):
        return MyClass.count


a=MyClass(5)
b=MyClass(10)
c=MyClass(250)

for obj in (a,b,c):
    print(obj.get_val())
    print(obj.get_count()) # Calling class variable
    print(obj.count) # Calling class variable directly from instance and instance looks within it first and then in class