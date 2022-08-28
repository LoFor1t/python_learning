import json

favorite_number = int(input("Enter you favorite number: "))

filename = 'json_files/favorite_number.json'

with open(filename, 'w') as f:
    json.dump(favorite_number, f)
