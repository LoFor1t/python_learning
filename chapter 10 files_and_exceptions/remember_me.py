import json

# username = input("What is your name? ")
#
# filename = 'json_files/username.json'
#
# with open(filename, 'w') as f:
#     json.dump(username.lower(), f)
#     print(f"We'll remember you when you come back, {username.title()}!")
#

# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.
# filename = 'json_files/username.json'
# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("What is your name? ")
#     with open(filename, 'w') as f:
#         json.dump(username.lower(), f)
#         print(f"We'll remember you when you come back, {username.title()}!")
# else:
#     print(f"Welcome back, {username.title()}!")


def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = 'json_files/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input("What is your name? ")
    filename = 'json_files/username.json'
    with open(filename, 'w') as f:
        json.dump(username.lower(), f)
    return username


def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username.title()}")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username.title()}")


greet_user()
