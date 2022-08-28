import json


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
    username = input("What is your name for saving? ")
    filename = 'json_files/username.json'
    with open(filename, 'w') as f:
        json.dump(username.lower(), f)
    return username


def get_current_name():
    username = input('What is your name?')
    return username


def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    current_username = get_current_name()
    if username == current_username:
        print(f"Welcome back, {username.title()}")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username.title()}")


greet_user()
