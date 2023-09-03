# Here we don't want our list to start from index 0 but want to start at index 1
class MyList(list):  # Inherit from list
    def __setitem__(self, index, value):
        if index==0:           
            raise IndexError  
        if index > 0:
            index = index-1
        super().__setitem__(index, value)

    def __getitem__(self, index):
        if index==0:
            raise IndexError
        if index > 0:
            index = index -1
            return super().__getitem__(index) # this method is called when we access
                                              # a value with subscript (x[1], etc.)
a=MyList([1,2,3,4]) # __init__() inherited from built-in list
print(a)     # __repr__() inherited from built-in list
a.append(5)  # append() ingerited from built-in list
print(a[1])  # (Mylist.__getitem__ customizes list super class) index is 1 but reflects 0
print(a[4])  # index is 4 but reflects 3


