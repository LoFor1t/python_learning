guest_list = ['Dracula', 'Mask', 'Walker']

print(f'Hello {guest_list[0]}, I want to invite you to my party!)')
print(f'Hello {guest_list[1]}, I want to invite you to my party!)')
print(f'Hello {guest_list[2]}, I want to invite you to my party!)')

print('We want to add new people to our list)')

guest_list.insert(0, 'Holland')
guest_list.insert(2, 'Shevtsov')
guest_list.append('Banana')

print(len(guest_list))