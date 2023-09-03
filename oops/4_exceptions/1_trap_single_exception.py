import sys

mydict = {'a':1, 'b':2, 'c':3, 'd':4}

key = input('please inputa a key: ')

try:
    print('Testing for Error')
    print("The value of {0} is {1}".format(key, mydict[key]))
    print("Everything is ok")
except KeyError:
    print('trapped error')
    print("the key {0} doesn't exist".format(key))
    #sys.exit()   # Incase we want to exit when it catches error
    
# What's most significant about our trapping this exception is that the program does not terminate

print("program continues")

