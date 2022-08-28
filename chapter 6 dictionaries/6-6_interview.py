favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phill': 'python',
}

names = ['vlad', 'jen', 'stella', 'anna', 'sarah']

for name in names:
    if name in favorite_languages.keys():
        print(f'{name.title()}, thank you for participation.')
    else:
        print(f"{name.title()}, please complete our interview.")
