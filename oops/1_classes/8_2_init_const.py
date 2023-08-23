class MyNum(object):
    def __init__(self, value):
        print("Running init function")
        try:
            self.val=int(value)
        except ValueError:
            value=0
        self.val=value

    def increment(self):
        self.val+=1


obj1=MyNum(5)
obj2=MyNum("Hi")

obj1.increment()
obj1.increment()
obj2.increment()
obj2.increment()
        
print(obj1.val)
print(obj2.val)
