import pickle

################################  Example-1 ##########################################################
mylist = ['a', 'b', 'c', 'd']

with open('./oops/5_object_serialization/datafile.txt', 'wb') as fh:
    pickle.dump(mylist, fh)    # One way to use pickle to save an object

with open('./oops/5_object_serialization/datafile.txt', 'rb') as fh:
    unpickled_list=pickle.load(fh)  # One way to use pickle to retrieve a saved object

print(unpickled_list)

###############################  Example-2 ###########################################################

x=pickle.dumps(['a', 'b', 1, 2.3]) # Second way to use pickle to save an object
var=pickle.loads(x)                # Second way to use pickle to retrieve a saved object
print(x)
print(var)

##############################  Example-3 ############################################################

this_int=555
this_string='oh my god'
this_dict_of_lists={
    'a':[1,2,3],
    'b':[4,5,6]
    }
this_list_of_tuples=[
    ('joe', 22, 'clerk'),
    ('pete', 34, 'salesman')
]

with open('./oops/5_object_serialization/datafile2.txt', 'wb') as fh:
    pickle.dump((this_int, this_string, this_list_of_tuples, this_dict_of_lists), fh)

with open('./oops/5_object_serialization/datafile2.txt', 'rb') as fh:
    tup=pickle.load(fh)

print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

##############################  Example-4 ############################################################

class MyClass(object):
    
    def __init__(self, init_val):
        self.val=init_val
    
    def increment(self):
        self.val +=1

cc=MyClass(5)
cc.increment()
cc.increment()

with open('./oops/5_object_serialization/datafile3.txt', 'wb') as fh:
    pickle.dump(cc, fh)  # We are taking the object cc and storing it in pickle by dumping it.

with open('./oops/5_object_serialization/datafile3.txt', 'rb') as fh:
    unpickled_cc=pickle.load(fh)

print(unpickled_cc)
print(unpickled_cc.val)

# So we were able to successfully store an instance and its state in a file which means that we could run the program later on open the file again and un-pickle the object and 
# just use it as if we had never stopped executing.

######################################################################################################


