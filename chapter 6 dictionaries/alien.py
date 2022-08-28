alien_0 = {'color': 'green',
           'points': 5}

print(alien_0['color'])
print(alien_0['points'])
print(f"You just earned {alien_0['points']} points)")

print('\n')

alien_0 = {'color': 'green'}
print(alien_0['color'])

print('\n')

alien_0 = {'color': 'green',
           'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print('\n')

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

print('\n')

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

print('\n')

alien_0 = {'x_position': 0,
           'y_position': 25,
           'speed': 'medium'}
print(f"Original x position: {alien_0['x_position']}")
# Пришелец перемещается вправо
# Вычисляем величину смещения на основании текущей скорости

if alien_0['speed'] == 'slow':
    increment = 1
elif alien_0['speed'] == 'medium':
    increment = 2
else:
    # Пришелец двигается быстро
    increment = 3
# Новая позиция равна сумме старой позиции и приращения

alien_0['x_position'] += increment
print(f"New x position: {alien_0['x_position']}")

print('\n')

alien_0 = {'color': 'green',
           'points': 5}
print(alien_0)

del alien_0['color']
print(alien_0)

