cities = {
    'kyiv': {
        'country': 'ukraine',
        'population': 2_884_000,
        'fact': 'capital of Ukraine',
    },
    'odessa': {
        'country': 'ukraine',
        'population': 993_120,
        'fact': 'the biggest port in Ukraine',
    },
    'kharkiv': {
        'country': 'ukraine',
        'population': 1_419_000,
        'fact': 'smartest city of Ukraine'
    }
}

for city, information in cities.items():
    print(f"Name - {city.title()}")
    print(f"Country - {information['country'].title()}")
    print(f"Population - {information['population']}")
    print(f"Fact - {information['fact']}")
    print('\n')
