import json
json_str='''
{
  "foo": "bar",
  "numbers": [{"one": 1}, {"two": 2}, {"tree": "NaN"}, {"foo": "NaN"}]
}
'''

# Turn the string into a "JSON" object
my_json = json.loads(json_str) # The JSON object is actually a Python dict

# Get the value of a key
foo = my_json['foo']
numbers = my_json['numbers']

# Get value of a key or a default one if the key doesn't exist
non_existent_key = my_json.get('blarg', 'default_value') 

# Add new key
my_json['bla'] = "bla"

# Update key
my_json['bla'] = "bleb"

# Delete a key
my_json.pop('foo')

# Append to `numbers`
my_json["numbers"].append({"xablau":"NaN"})

# Get all non "NaN"s from `numbers`
non_nans = []
for number_dict in my_json["numbers"]:
    for value in number_dict.values():
        if value != "NaN":
            non_nans.append(number_dict)

# Convert JSON dict to a valid JSON string
json_str_final = json.dumps(my_json)
