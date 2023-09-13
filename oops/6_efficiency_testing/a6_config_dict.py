import os
import pickle

class ConfigKeyError(Exception):

    def __init__(self, this, key): # here "this" is the config dict object and "self" is config key error object
        self.key=key
        self.keys=this.keys()
    def __str__(self):
        return 'key"{0}" not found. Available keys: ({1})'.format(self.key, ','.join(self.keys))


class ConfigDict(dict):

    config_directory='./oops/5_object_serialization/'

    def __init__(self, filename):

        self._filename=os.path.join(ConfigDict.config_directory,filename + '.pickle')     # setting the name of the file in the instance as a private attribute

        if not os.path.isfile(self._filename):  # verifying if the file exists
            with open(self._filename,'w') as fh:
                pickle.dump({}, fh)  # creating an empty dictionary and create file if not exist

        with open(self._filename) as fh:   # reading each line from file to dict in current instance
            file_dict=pickle.load(fh)
            self.update(file_dict) # this basically updates the instance dict with the loaded pickle object which in this case is an empty dictionary

    def __setitem__(self, key, value):
        super().__setitem__(key, value)   # setting the new key and new value in the instance
        with open(self._filename, 'w') as fh:
            pickle.dump(self, fh)

    def __getitem__(self, key):
        if not key in self:
            raise ConfigKeyError(self, key)
        return super().__getitem__(key)   # reading the value of key from the instance
                    