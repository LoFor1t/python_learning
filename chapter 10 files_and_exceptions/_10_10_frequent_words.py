filename = 'text_files/little_women.txt'

with open(filename) as f_obj:
    string = f_obj.read()
    print(string.count('the'))
    print(string.lower().count('the'))
    print(string.count('the '))
    print(string.lower().count('the '))
