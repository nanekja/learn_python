class MyClass(object):

    def __enter__(self):            # this magic metod is called as soon as enter with block
        print("we have entered with")
        return self

    def __exit__(self, type, value, traceback): # this method is called before leaving with block which can also capture exceptions
        print("we are leaving with")

    def sayhi(self):
        print("hi, instance {0}".format(id(self)))

with MyClass() as a:
    a.sayhi()

print('after the with block')
