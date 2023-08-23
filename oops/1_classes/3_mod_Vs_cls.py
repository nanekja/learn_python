# A python module is simply a file that contains code.
# This code can be executed directly or it can be imported

import mymod

print(mymod.var)
mymod.welcome()

# A Class is simply a python code
# The designers of the Decimal class decided to name the module decimal and 
# the class that's inside the module.

from decimal import Decimal

print(Decimal(3.5)+Decimal(3.5))

# the lower case decimal is the module and the upper case Decimal is the class that's 
# inside the decimal module.
# All classes begin with an uppercase letter