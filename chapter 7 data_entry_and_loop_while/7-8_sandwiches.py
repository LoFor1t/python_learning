sandwich_orders = ['panini', 'lviv', 'bbq']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"I made your {finished_sandwich} sandwich.")
    finished_sandwiches.append(finished_sandwich)

print("The list of made sandwiches: ")
for finished_sandwich in finished_sandwiches:
    print(f'\t{finished_sandwich.title()}')
