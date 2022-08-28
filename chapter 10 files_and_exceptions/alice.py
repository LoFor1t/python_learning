filename = 'text_files/alice.txt'
#
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     msg = f"Sorry, the file {filename} does not exists."
#     print(msg)

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = f"Sorry, the file {filename} does not exist/"
    print(msg)
else:
    # Подсчёт приблизительного количества строк в файле.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")




