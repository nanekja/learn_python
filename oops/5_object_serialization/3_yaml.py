import yaml
import json

################################  Example-1 ##########################################################

mydict={'a': 1, 'b': 2, 'c': 3}
mylist=[1,2,3,4,5]
mytuple=('x','y','z')

loaded_yaml=yaml.dump(mydict, default_flow_style=False)
print(loaded_yaml)

print(yaml.dump(mylist, default_flow_style=False))
print(yaml.dump(mytuple, default_flow_style=False))

###############################  Example-2 ###########################################################

myobj = (
    [1,2,3,4,5],
    {'a':1, 'b':2, 'c':3},
    ('cat', 'dog'),
    [
        {'x': 98, 'y': 99, 'z': 100},
        8,
        7
    ],
    {'a': [1,2,3], 'b': [4,5,6], 'c': [7,8,9]}
)
print(yaml.dump(myobj, default_flow_style=False))

###############################  Example-3 ###########################################################

with open('./oops/5_object_serialization/app.yml') as fh:
    struct=yaml.safe_load(fh)

print(struct)
print(json.dumps(struct, indent=4, separators=(',', ': ')))

###############################  Example-4 ###########################################################

class MyClass(object):

    classvar=10

    def __init__(self, init_val):
        self.val=init_val

    def increment(self):
        self.val +=1

cc=MyClass(5)
cc.increment()
cc.increment()

with open('./oops/5_object_serialization/obj.yaml', 'w') as fh:
    yaml.dump(cc, fh)

with open('./oops/5_object_serialization/obj.yaml') as fh:
    obj_cc=yaml.unsafe_load(fh)

print(obj_cc.val)
