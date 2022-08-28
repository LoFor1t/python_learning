list_of_numbers = []
list_of_ordinals = []

for i in range(1, 11):
    list_of_numbers.append(str(i))

for number in list_of_numbers:
    if number == '1':
        ordinal = number + 'st'
    elif number == '2':
        ordinal = number + 'nd'
    elif number == '3':
        ordinal = number + 'rd'
    else:
        ordinal = number + 'th'
    print(ordinal)



