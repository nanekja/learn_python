class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val=self.filterint(val)
        InstanceCounter.count +=1

    @staticmethod           # This is a utility method
    def filterint(value):
        if not isinstance(value, int):
            return 0
        else:
            return value

a=InstanceCounter(3)
b=InstanceCounter("hi")
c=InstanceCounter(13)

for obj in (a,b,c):
    print(obj.val)
