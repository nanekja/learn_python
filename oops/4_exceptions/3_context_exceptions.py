# Here we're seeing a series of calling contexts. Every time we enter a function we're said to
# enter a context and when an error occurs Python is aware of the context we're in.

class MyClass(object):

    @staticmethod
    def make_error():
        print('entering make error()')
        5/0
        print('leaving make_error()')

    def do_something(self):
        print('entering do_something()')
        self.make_error()
        print('leaving do_something()')

def some_util_func():
    print('entering some_util_func()')
    a=MyClass()
    a.do_something()
    print('leaving some_util_func()')

def some_major_func():
    print('entering some_major_func()')
    some_util_func()
    print('leaving some_major_func()')

def main():
    print('entering main()')
    some_major_func()
    print('leaving main()')

try:
    main()
except ZeroDivisionError:
    print("OOPS")

# When an error is raised, we see what's called a stack trace. It traces the stack of calls which
# led us to this point in the code calling. It refers to each of the function or method calls that
# occurred along the way and it's called a stack because when we enter a function we're entering a new
# context where we haven't yet completed execution of the old context.
# the order in which the calls were made and the last call will be the most recent one that was 
# made and that's when we get this exception. Now what's particularly useful about exceptions and 
# calling contexts is that the error can be trapped at any call at any place along the call stack.
