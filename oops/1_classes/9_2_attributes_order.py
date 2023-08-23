class MyClass(object):
    classy=10

obj1=MyClass()

print(obj1.classy) # here it prints the value of class attribute

obj1.classy="hi" # Assigning value to instance attribute

print(obj1.classy) # Here python will try to fetch the value of the attribute in the instance first and then in the class

del obj1.classy # Here the instance attribute value is deleted

print(obj1.classy) # Here python once again fetches value from class as the instance attribute is not available anymore