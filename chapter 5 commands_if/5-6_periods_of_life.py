name = None
age = int(input('My age is: '))

if age < 2:
    name = 'small baby'
elif age < 4:
    name = 'baby'
elif age < 13:
    name = 'child'
elif age < 20:
    name = 'teenager'
elif age < 65:
    name = 'adult'
elif age >= 65:
    name = 'old man'
print(f'You are {name}!')
