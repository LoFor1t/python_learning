file_name = 'pi_digits.txt'
with open(f'text_files/{file_name}') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print('\n')

with open(f"text_files/{file_name}") as file_object:
    for line in file_object:
        print(line.rstrip())

print('\n')

with open(f"text_files/{file_name}") as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print('\n')

with open(f"text_files/{file_name}") as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

print('\n')

file_name = 'pi_million_digits.txt'

with open(f"text_files/{file_name}") as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

print('\n')

with open(f"text_files/{file_name}") as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday? in the fom ddmmyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
    # print(pi_string.index(birthday))
else:
    print("Your birthday does not appear in the first million digits of pi.")
