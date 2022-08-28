file_name = 'learning_python.txt'

with open(f"text_files/{file_name}") as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace('Python', 'C'))
