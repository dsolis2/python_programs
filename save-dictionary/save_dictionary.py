# 1. Function to Save a dictionary to a file
# 2. Function open the file and read dictionary and return the dictionary object
# if functions are in separate file
# Use the following: from function_file import function_name

import json
 
test_dict = {"one":1, "two":2,"three":3}
file = 'dictionary.txt'

def save_dict(d,f):
    json.dump(d, open(f,'w'))

def load_dict(f):
    d = json.load(open(f))
    return d

save_dict(test_dict,file)
recover = load_dict(file)
print('Recovered data: ', recover)