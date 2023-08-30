import abc

class GetSetParent(object):
    __metaclass__ = abc.ABCMeta   #getsetparent will be an abstract base class through the metaclass attribute which means that getsetparent can't be instantiated directly.

    def __init__(self,value):
        self.val=0

    def set_val(self, value):
        self.val=value

    def get_val(self):
        return self.val

    @abc.abstractmethod
    def showdoc(self): # this is the only abstract method in this abstract base class which is requried in subclasses
        return


class GetSetInt(GetSetParent):   #This inherits from getsetparent class and this class has only 2 out of 4 classes from parent

    def set_val(self, value): # here set_val extends the behaviour of set_val in parent class
        if not isinstance(value, int):
            value=0
        super().set_val(value)    # here we are calling the set_val method in the parent without the explicit naming it directly

    def showdoc(self):  # this method is mandatory to be called as it is defined as abstract method
        print('GetSetInt object ({0}), only accepts integer values'.format(id(self)))


class GetSetList(GetSetParent):

    def __init__(self, value=0):
        self.vallist = [value]

    def get_val(self):   # here we are overriding the get_val definition of parent class
        return self.vallist[-1]

    def get_vals(self):
        return self.vallist

    def set_val(self, value):
        self.vallist.append(value)

    def showdoc(self):  # Though most of above methods are not inheriting from parent, it is a contract as we have an abstract method to be used
        print('GetSetList object, len{0}, stores history of values set'.format(len(self.vallist)))


x=GetSetInt(3)
print(x.get_val())
x.set_val(5)
print(x.get_val())
x.showdoc()

gsl=GetSetList(5)
gsl.set_val(10)
gsl.set_val(20)
print(gsl.get_val())
print(gsl.get_vals())
gsl.showdoc()

