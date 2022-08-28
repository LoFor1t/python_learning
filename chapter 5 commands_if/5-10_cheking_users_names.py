current_users = ['Iryna', 'Nataliya', 'Viktoriya', 'Joe', 'Vlad']

new_users = ['Carl', 'Joe', 'Chris', 'Vlad', 'Robert']

for increment in range(len(current_users)):
    current_users[increment] = current_users[increment].lower()


for new_user in new_users:
    if new_user.lower() in current_users:
        print('This name is reserved, please write new)')
    else:
        print(f"Name {new_user} isn't reserved)")