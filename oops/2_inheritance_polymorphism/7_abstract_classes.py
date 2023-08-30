import abc # The ABC module imported up here provides facilities for creating abstract base classes which are classes 
           # that are not designed to be instantiated but only to be subclassed.

class GetterSetter(object):
    __metaclass__=abc.ABCMeta   # metaclass can define other classes. Here we're basically saying that this 'GetterSetter' should be defined as an abstract base class

    @abc.abstractmethod         # This is to indicate that it is an abstract method
    def set_val(self, input):
        """Set a value in the instance"""
        return

    @abc.abstractmethod
    def get_val(self):
        """Return a value from instance"""
        return

class MyClass(GetterSetter):

    def set_val(self, input):
        self.val=input

    def get_val(self):
        return self.val

x=MyClass()
print(x)
