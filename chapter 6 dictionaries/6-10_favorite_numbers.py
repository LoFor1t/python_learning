favorite_numbers = {
    'Joe': [5, 26],
    'Allie': [12, 23],
    'Carl': [18],
    'Michele': [24, 2],
    'Alice': [85],
}

for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
            verb = 'number is'
    else:
            verb = 'numbers are'
    print(f"{name.title()} favorite {verb}:")
    for number in numbers:
        print(f'\t{number}')
    print('\n')


