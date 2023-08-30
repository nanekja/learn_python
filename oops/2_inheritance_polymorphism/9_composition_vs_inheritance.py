import random
from io import StringIO

class WriteMyStuff(object):

    def __init__(self, writer):   # The init method simply accepts the writer object as the file handle or the string IO object and 
        self.writer=writer        # stores it in the object under the attribute writer

    def write(self):
        write_text="This is a silly message"
        self.writer.write(write_text)  # Notice that write doesn't check type of writer to see if it is a file object or a string IO object. This is polymorphic

# So we could make changes to any of these classes and internal changes won't make a difference to write. So the benefit here is that we don't have to be worried about a class hierarchy.

fh = open('test.txt', 'w')
w1 = WriteMyStuff(fh)
w1.write()
fh.close()

# Now we will have a string IO class which writes to a string buffer. String buffer is just a string but it's an object that we can write to as if it was a file.
# It's a little like concatenation except that it's presumably more efficient and it gives us the interface to a string that we would normally find in a file object specifically the write method.

s_io=StringIO()
w2=WriteMyStuff(s_io)
w2.write()

print('file object:', open('test.txt', 'r').read())
print('String object: ',s_io.getvalue())

