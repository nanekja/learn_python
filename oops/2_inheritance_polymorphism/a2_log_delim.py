import abc
import datetime

class WriteFile(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, filename):
        self.file = filename

    @abc.abstractmethod
    def write(self):
        return

    def write_line(self, text):
        fh = open(self.file, 'a')
        fh.write(text + '\n')
        fh.close

class LogFile(WriteFile):
    def write(self, value):
        dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        super().write_line('{0} {1}'.format(dt_str,value))

class DelimFile(WriteFile):
    def __init__(self, filename, delim):
        super().__init__(filename)
        self.delim=delim

    def write(self, value):
        line = self.delim.join(value)
        super().write_line('{0}'.format(line))







        

