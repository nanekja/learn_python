class MyDict1(dict):
    pass

a=MyDict1()
a['x']=5
a['y']=6
for key in a:
    print('{0}={1}'.format(key, a[key]))

class MyDict2(dict):
    def __setitem__(self, key, value):
        print("I'm in 1st dict")        # here we are extending the functionality of built-in methods of dict
        super().__setitem__(key, value)

b=MyDict2()
b['x']=9
b['y']=10
for key in b:
    print('{0}={1}'.format(key, b[key]))