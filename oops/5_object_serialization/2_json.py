import json

################################  Example-1 ##########################################################

with open('./oops/5_object_serialization/backup_config.json') as fh:
    conf=json.load(fh)

print(conf)

conf['newkey']=10.0001

with open('./oops/5_object_serialization/backup_config.json', 'w') as fh:
    json.dump(conf, fh, indent=4, separators=(',', ': '))

###############################  Example-2 ###########################################################

x=json.dumps({'a':[1,2,3], 'c':[7,8,9], 'b':[4,5,6]})
print(x)
