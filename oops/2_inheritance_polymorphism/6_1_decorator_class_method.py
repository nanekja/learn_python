class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val=val
        InstanceCounter.count +=1

    def set_val(self,newval):
        self.val=newval

    def get_val(self):
        return self.val

    @classmethod         # This is a decorator which is a processor that modifies a function. It modifies the default binding that instance methods provide
    def get_count(cls):  # A class method takes the class (not instance) as argument and works with the class object
        return cls.count

a=InstanceCounter(5)
b=InstanceCounter(11)
c=InstanceCounter(19)

for obj in (a,b,c):
    print(obj.get_val())
    print(obj.get_count())

print(InstanceCounter.count)
