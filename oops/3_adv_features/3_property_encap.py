class GetSet(object):

    instance_count=0  # public variable with appropriate naming convention

    __mangled_name = 'no privacy!'  # This is the special private variable which is not intended to be subclassed and represented with appropriate naming convention

    def __init__(self, value):
        self._attrval=value      # private variable with appropriate naming convention
        GetSet.instance_count +=1

    @property   # Here @property decorator applied to the var() method. The var() method returns the private instance attribute value attrval
    def var(self):
        print("Getting the 'var' attribute")
        return self._attrval

    @var.setter
    def var(self, value):
        print("Setting the 'var' attribute")
        self._attrval=value

    @var.deleter
    def var(self):
        print("Deleting the 'var' attribute")
        self._attrval=None

a=GetSet(5)
a.var=100
print(a.var)
del a.var
print(a.var)

b=GetSet(5000)
b.var=10000
print(b._attrval) # Notice we are still be able to access private attribute as its not Pythonic to enforce. It's just to let user know that its private and is not intended to be used externally
print(b._GetSet__mangled_name) # this is not intended to be subclassed and as you can see you can't just retrieve it by 'b__mangled_name' and you had to mention class name. This is also to let user know

