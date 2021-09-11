# This example shows how to work with JSON in Python
import json

address = {}
address["humpty"]= {
        'road' : 'abc',
        'city' : 'bangalore',
        'pincode':'111111'
    }
address["dumpty"]= {
        'road' : 'xyz',
        'city' : 'pune',
        'pincode':'222222'
    }

# dump dict as JSON string
address_json = json.dumps(address)

# write the JSON string in a file in same folder
with open("address.txt","w") as f:
    f.write(address_json)

# read content of the file in a JSON string
my_address = open("address.txt","r").read()

# convert JSON string to a dictionary
my_address_dict = json.loads(my_address)

# get pincode for an address
print(my_address_dict['dumpty']['pincode'])
