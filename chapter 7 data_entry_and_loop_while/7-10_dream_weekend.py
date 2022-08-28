dream_weekend = {}

while True:
    name = input('Your name: ')
    place = input('Place, where do you want have a dream weekend: ')
    dream_weekend[name] = place

    flag = input('Do you want to ask other human? (yes/ no) ')
    if flag == 'no':
        break

for name, place in dream_weekend.items():
    print(f"{name.title()} want to spend his dream weekend in {place.title()}.")