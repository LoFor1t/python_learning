def build_person(first_name, last_name, age=''):
    """Возвращает словарь с информацией о человеке."""
    person = {
        'first': first_name,
        'last': last_name
    }
    if age:
        person['age'] = age
    return person


print(build_person('Alla', 'Johnson', 15))
