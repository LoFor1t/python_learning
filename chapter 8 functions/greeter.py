# def greet_user():
#     """Выводит простое приветствие."""
#     print("Hello!")
#
#
# greet_user()
#
# def greet_user(username):
#     """Выводит простое приветствие."""
#     print(f"Hello, {username.title()}!")
#
#
# greet_user('vlad')


def get_formatted_name(first_name, last_name):
    """Возвращает аккуратно отформатированное полное имя."""
    full_name = f"{first_name.title()} {last_name.title()}"
    return full_name


while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(formatted_name)

