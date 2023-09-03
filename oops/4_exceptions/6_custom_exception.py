# Here we wish to raise an exception of a certain type for example if a user calls one of our functions that requires a date in a certain format 
# We can validate the format and raise a python built in exception if it's incorrect

import re

def process_date(this_date):
    # this regex makes sure that this_date is YYYY-MM-DD
    if not re.search(r'\d\d\d\d-\d\d-\d\d$', this_date):    # \d	Returns a match where the string contains digits (numbers from 0-9). Signals a special sequence 
        raise ValueError('please submit date in YYYY-MM-DD format') # Here We've also placed a message into the argument value where this becomes part of the message attribute

    print('the submitted date is {0}'.format(this_date))

process_date('1980-01-03')

process_date('1/3/1980')
