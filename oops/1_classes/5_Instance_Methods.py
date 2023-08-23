
class SomeClass(object):
    sometext= 'someone happy'

someobj = SomeClass()

print(someobj.sometext)

# Now we shall see that the class methods being called by an instance

class EveryoneClass(object):
    def new_method(self):
        print("I came from new_method")
        print(self)

new_obj = EveryoneClass()
new_obj.new_method()
print(new_obj)

# The instance gets passed as the first argument automatically. This is a default implicit behavior.
# When a method is called on an instance the instance is passed as the implicit first argument.
# This is represented with "self" argument in the method
# We can notice the hex code of self and instance are identical. So we can confirm that both
# are same that is self and instance


