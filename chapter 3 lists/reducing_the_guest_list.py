guest_list = ['Dracula', 'Mask', 'Walker']

print(f'Hello {guest_list[0]}, I want to invite you to my party!)')
print(f'Hello {guest_list[1]}, I want to invite you to my party!)')
print(f'Hello {guest_list[2]}, I want to invite you to my party!)')

print('We want to add new people to our list)')

guest_list.insert(0, 'Holland')
guest_list.insert(2, 'Shevtsov')
guest_list.append('Banana')

for i in guest_list:
    print(f'Hello {i}, I want to invite you to my party!')

print('On my party can be only 2 famous person(')

while len(guest_list) > 2:
    no_needed_guest = guest_list.pop()
    print(f"Sorry {no_needed_guest}, but you can't go to my party")


for i in guest_list:
    print(f'Hello {i}, I want to invite you to my party!')

for i in range(len(guest_list)):
    print(i)
    del guest_list[i]

print(guest_list)
