import json

filename = 'json_files/favorite_number.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    favorite_number = int(input("Enter your favorite number: "))
    with open(filename, 'w') as f:
        json.dump(number, f)
else:
    print(number)

