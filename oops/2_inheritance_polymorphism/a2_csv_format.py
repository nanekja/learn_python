from datetime import datetime

class WriteFile(object):
    def __init__(self, filename, writer):
        self.fh=open(filename, 'w')
        self.formatter=writer()

    def write(self, text):
        self.fh.write(self.formatter.format(text))
        self.fh.write('\n')

    def close(self):
        self.fh.close()

class CSVFormatter(object):
    
    def __init__(self):
        self.delim=','

    def format(self, this_list):
        new_list = []
        for i in this_list:
            if self.delim in i:
                new_list.append('"{0}"'.format(i))
            else:
                new_list.append(i)
        return self.delim.join(new_list)

class LogFormatter(object):

    def format(self, this_line):
        date_str=datetime.now().strftime('%Y-%m-%d %H:%M')
        return "{0} {1}".format(date_str,this_line)

                