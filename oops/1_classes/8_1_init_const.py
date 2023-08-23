class MyNum(object):
    def __init__(self):
        self.val=0
        print("Running init function")
    def increment(self):
        self.val +=1


a_obj=MyNum()
a_obj.increment()
print(a_obj.val)

a_obj.increment()
print(a_obj.val)

