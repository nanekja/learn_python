class SumList(object):

    def __init__(self, mylist):
        self.mylist=mylist

    def __add__(self, other):
        new_list=[x+y for x,y in zip(self.mylist, other.mylist)]
        return SumList(new_list)

    def __repr__(self):
        return str(self.mylist)

a = SumList([100, 200, 300, 400, 500])
b = SumList([1,2,3,4,5])

c=a+b           # here its doing c=a.__add__(b)
print(c)