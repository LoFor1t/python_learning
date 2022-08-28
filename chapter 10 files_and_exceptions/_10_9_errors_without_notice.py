filenames = ['cats.txt', 'dogs.txt', 'fakfkas.txt']

for file in filenames:
    try:
        with open(f"text_files/{file}") as f_obj:
            names = f_obj.readlines()
    except FileNotFoundError:
        pass
    else:
        for name in names:
            print(name.title().strip())
    print('\n')
