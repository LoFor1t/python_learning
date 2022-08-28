# def count_words(filename):
#     """Подсчет приблизительного количества строк в файле."""
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read()
#     except FileNotFoundError:
#         msg = f"Sorry, the file {filename} does not exist."
#         print(msg)
#     else:
#         # Подсчет приблизительного количества строк в файле.
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {filename} has about {num_words} words.")
#
#
# filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
# for file in filenames:
#     count_words(f"text_files/{file}")

def count_words(filename):
    """Подсчет приблизительного количества строк в файле."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Подсчет приблизительного количества строк в файле.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for file in filenames:
    count_words(f"text_files/{file}")
