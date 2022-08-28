alien_0 = {
    'color': 'green',
    'points': 5,
}
alien_1 = {
    'color': 'yellow',
    'points': 10,
}
alien_2 = {
    'color': 'red',
    'points': 15,
}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print('\n')

# Создание пустого списка для хранения пришельцев.
aliens = []

# Создание 30 зелёных пришельцев
for i in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
    }
    aliens.append(new_alien)

# Вывод первых 5-ти пришельцев:

for alien in aliens[:5]:
    print(alien)
print('...')

print(f"Total number of aliens - {len(aliens)}")

print('\n')

# Создание пустого списка для хранения пришельцев.
aliens = []

# Создание 30 зелёных пришельцев
for i in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow',
    }
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

# Вывод первых 5-ти пришельцев.
for alien in aliens[:5]:
    print(alien)
print('...')


print('\n')

# Создание пустого списка для хранения пришельцев.
aliens = []

# Создание 30 зелёных пришельцев
for i in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow',
    }
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

# Вывод первых 5-ти пришельцев.
for alien in aliens[:5]:
    print(alien)
print('...')
