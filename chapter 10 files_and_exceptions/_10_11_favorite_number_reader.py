import json

filename = 'json_files/favorite_number.json'

with open(filename) as f:
    string = json.load(f)

print(string)
