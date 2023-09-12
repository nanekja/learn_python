import timeit

################################  Example-1 ##########################################################

# There are two ways to call time. What can retrieve a value from a dictionary more quickly by using a subscript or by using get
# We're going to execute the code snippet 1 million times not the setup but the statement.

print('by index: ', timeit.timeit(stmt="mydict['c']", setup="mydict={'a':5, 'b':6,'c':7}", number=1000000))
print('by get: ', timeit.timeit(stmt="mydict.get('c')", setup="mydict={'a':5, 'b':6,'c':7}", number=1000000))

# run the code multiple times to see which one runs faster

################################  Example-2 ##########################################################

# here's how we might call time it if we wanted to test a call to a function

def testme(this_dict, key):
    return this_dict[key]

print(timeit.timeit("testme(mydict, key)", setup="from __main__ import testme; mydict={'a':1, 'b':2, 'c':3}; key='c'", number=10000))