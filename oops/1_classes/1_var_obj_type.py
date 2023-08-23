# In Python everything is an object including primitives

# An object is an entity that holds data in the form of attributes.
# It is of a particular class or type and is associated with functionality in the form of methods
# Primitives like integers are objects in Python

# The type function returns the type of any Python's objects.

mylist = ['a', 'b', 'c']
myint = 5
mystr = 'King'
mybool = True
mynone = None

def myfunc():
    print('hello')

this_type = type(mylist)

print(type(mylist))
print(type(myint))
print(type(mystr))
print (type(mybool))
print (type(mynone))
print (type(myfunc))
print(type(this_type))

# So indeed every single object in Python has a type including the none value which 
# is Python's null value it's of type none type.
# The function to is a variable that has a type.
# The type of the list was assigned to a variable and then the type of that object has a type 'type'.
