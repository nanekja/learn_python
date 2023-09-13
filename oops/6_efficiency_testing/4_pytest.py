############## in a file called myprogram.py ############ This is the progra which we wanted to test
import sys

def doubleit(x):
    var=x * 2
    return var

if __name__ == '__main__':     #This gate basically says that if we execute the program containing this directly, then we will execute all the lines under it
    # But if we import the program containing this gate from another script, then all of the code from this program will get loaded but the code under this gate won't get executed

    input_val = sys.argv[1]
    doubled_val=doubleit(input_val)

    print("The value of {0} is {1}".format(input_val, doubled_val))


############### in a file called test_myprogram.py ############ This is the testing program
# The name "test" prepended to the name of our script and our function is required for Python to be able to find it when we first run pytest
import myprogram

def test_doubleit():
    assert myprogram.doubleit(10)==20
