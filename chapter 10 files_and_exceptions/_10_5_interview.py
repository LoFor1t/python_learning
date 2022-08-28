file_name = 'text_files/interview.txt'

with open(file_name, 'w') as file_object:
    while True:
        reason = input("Why do you like programming - ")
        if reason == 'q':
            break
        else:
            file_object.write(reason + '\n')
