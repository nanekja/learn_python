from a3_configdict import ConfigDict

a=ConfigDict('./oops/3_adv_features/config_file.txt')

print(a['sql_query'])

print(a['email_to'])

a['database']='mysql_managed'

print(a)

