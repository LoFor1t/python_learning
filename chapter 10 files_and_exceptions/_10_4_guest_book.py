file_name = 'text_files/quest_book.txt'

with open(file_name, 'w') as file_object:
    while True:
        name_guest = input("Please enter your name - ")
        if name_guest == 'q':
            break
        else:
            file_object.write(name_guest.title() + '\n')
