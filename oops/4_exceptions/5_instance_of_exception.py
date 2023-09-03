mydict = {'a':1, 'b':2}

try:
    print(5/0)
except ZeroDivisionError as e: # If we go with exception error as a variable that variable is an instance of this exception class
    
    print(e.message) # You'll see that message is the message that Python is displaying or 
                     # that it would display if we didn't trap the error
    print(e.args)    # ARGs is a tuple which just contains the messages.
