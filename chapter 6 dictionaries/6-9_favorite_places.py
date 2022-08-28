favorite_places = {
    'home': ['Bob'],
    'school': ['Kevin', 'Bob', 'Stuart'],
    'walk': ['Stuart', 'kevin']
}

for place, people in favorite_places.items():
    for name in people:
        print(f"{name.title()} like {place.title()}")
