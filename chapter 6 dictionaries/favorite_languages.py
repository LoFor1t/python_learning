favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phill': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

print('\n')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phill': 'python',
}

for name in favorite_languages.keys():
    print(name.title())

print('\n')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phill': 'python',
}

friends = ['phill', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(f"    Hi {name.title()}, I see your favorite language is {favorite_languages[name].title()}.")

print('\n')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phill': 'python',
}

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')

print('\n')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phill': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print('\n')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phill': 'python',
}

print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())

print('\n')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phill': 'python',
}

print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())

print('\n')


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phill': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        verb = 'language is'
    else:
        verb = 'languages are'
    print(f"\n{name.title()}'s favorite {verb}:")
    for language in languages:
        print(f"\t{language.title()}")
