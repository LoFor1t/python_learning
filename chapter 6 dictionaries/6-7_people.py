human_1 = {
    'first_name': 'Stella',
    'last_name': 'Havrilova',
    'age': 17,
    'city': 'Kyiv',
}
human_2 = {
    'first_name': 'Carl',
    'last_name': 'De-Santa',
    'age': 55,
    'city': 'LA',
}
human_3 = {
    'first_name': 'Trevor',
    'last_name': 'Johnson',
    'age': 64,
    'city': 'Liberty City',
}

people = [human_1, human_2, human_3]

for human in people:
    print(f"First name - {human['first_name']}")
    print(f"Last name - {human['last_name']}")
    print(f"Age - {human['age']}")
    print(f"City - {human['city']}")
    print('\n')
