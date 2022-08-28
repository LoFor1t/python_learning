filenames = ['cats.txt', 'dogs.txt']

for file in filenames:
    try:
        with open(f"text_files/{file}") as f_obj:
            names = f_obj.readlines()
    except FileNotFoundError:
        print(f"Sorry, file {file} not found(")
    else:
        for name in names:
            print(name.title().strip())
    print('\n')
