pizzas = ['Paperoni', 'Italian', 'Hawaiian']
friend_pizzas = pizzas[:]

pizzas.append('Carbonara')
friend_pizzas.append('Vegeterian')

print('My favourite pizzas are: ')
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favourite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)

