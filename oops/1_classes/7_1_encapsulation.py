

class MyClass(object):
    def set_val(self, val):
        self.value=val

# set_val uses 2 arguments because any instance method that is a method designed to work on the instance implicitly
# and invisibly passes the instance as the first argument to the method.

    def get_val(self):
        return self.value

a_obj = MyClass()
b_obj = MyClass()

# The following is the way to assign attribute via self in the method
a_obj.set_val(10)
b_obj.set_val(20)
# The following is the way to directly assigning attribute in the instance
a_obj.value = 'hi'

# The reason we generally assign attributes via method and not directly is that using such methods provides a kind of a gateway for any operations having to do with
# the instances state.
# And in this gateway we can ensure the integrity of the instances attributes by using these methods we're encapsulating the instance and ensuring the integrity of its data.

print(a_obj.get_val())
print(b_obj.get_val())

# Notice that the attribute assigned directly in the instance takes precedence over the attribute assigned via the method in class