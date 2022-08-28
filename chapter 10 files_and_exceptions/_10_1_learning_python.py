file_name = 'learning_python.txt'

with open(f"text_files/{file_name}") as file_object:
    print(file_object.read().rstrip())

print('\n')

with open(f"text_files/{file_name}") as file_object:
    for line in file_object:
        print(line.rstrip())

print('\n')

with open(f"text_files/{file_name}") as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
