bob = {
    'breed': 'corgi',
    "owner's_name": 'Vlad'
}
cevin = {
    'breed': 'pug',
    "owner's_name": 'Dima'
}
stuart = {
    'breed': 'chihuahua',
    "owner's_name": 'Aleks'
}

pets = [bob, cevin, stuart]

for pet in pets:
    print(f"Breed - {pet['breed'].title()}")
    print("Owner's name - " + str(pet["owner's_name"]))
    print('\n')
