# When we raise an exception we're really constructing an exception instance which will have attributes just like any other instance
# Like all other built-in class extensions, we can create our own exception classes. We would do this in order to have our exception do more work than just display an error message
# Although usually a custom class won't do a great deal more than display a message, that type of error
# is itself significant of course and we often create our own error types so that we can indicate a particular situation that Python doesn't normally cover.

class MyError(Exception): # Here MyError class inherits from built-in Exception class
# The two basic methods __init__ and __str__ are automatically called during the exception handling process. Usually they're called in close succession

# __init__ is called when the instance is created
    def __init__(self, *args): # here args is capturing any arguments that are passed to MyError
        print("Calling init")
        if args:
            self.message=args[0]
        else:
            self.message=''

# __str__ is called when the exception is raised
    def __str__(self):
        print("Calling str")
        if self.message:
            return("here's a MyError exception with a message : {0}".format(self.message))
        else:
            return("here's a MyError exception!")

raise MyError
raise MyError("Houston, we have a problem")
