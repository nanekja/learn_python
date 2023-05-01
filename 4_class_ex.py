# Sample class creation

class MyClass(object):
    pass

this_obj = MyClass()
print(this_obj)

that_obj = MyClass()
print(that_obj)

# In the above output we can notice that we get 2 different hex codes for the 2 objects. This tells
# that both objects are seperate/different


# We've now added a variable 'var' to YourClass

class YourClass(object):
    var = 10

your_obj = YourClass()
our_obj = YourClass()

print(your_obj.var)
print(our_obj.var)

# So when we ask for an attribute from an instance the instance looks for that 
# attribute in the class
# we've shown that variables defined in the class are available in the instances 
# through object.attribute syntax.

