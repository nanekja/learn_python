import os

class ConfigKeyError(Exception):
    def __init__(self, this, key): # here "this" is the config dict object and "self" is config key error object
        self.key=key
        self.keys=this.keys()
    def __str__(self):
        return 'key"{0}" not found. Available keys: ({1})'.format(self.key, ','.join(self.keys))


class ConfigDict(dict):
    def __init__(self, filename):
        self._filename=filename     # setting the name of the file in the instance as a private attribute
        if not os.path.isfile(self._filename):  # verifying if the file exists
            try:
                open(self._filename,'w').close()
            except IOError:
                raise IOError('arg to ConfigDict must be a valid pathname')
        with open(self._filename) as fh:   # reading each line from file to dict in current instance
            for line in fh:
                (key, val)=line.rstrip().split("=",1) # here we are first striping the each line that is it will strip \n and then split the line at the 1st occurance of =
                super().__setitem__(key,val)  # setting the key and value in the instance

    def __setitem__(self, key, value):
        super().__setitem__(key, value)   # setting the new key and new value in the instance
        with open(self._filename, 'a') as fh:
            for key, value in self.items():
                fh.write('\n{0}={1}'.format(key,value))  # writing the new key and new value to the file

    def __getitem__(self, key):
        if not key in self:
            raise ConfigKeyError(self, key)
        return super().__getitem__(key)   # reading the value of key from the instance
                    