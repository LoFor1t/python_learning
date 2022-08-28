glossary = {
    'variable': 'this is a container, which can have in itself any information.',
    'boolean expression': 'this is expression, which can have only True or False',
    'integer': 'it is type of dates which can have only numbers',
    'string':  ' it is type of dates which can have any symbols',
    'list': 'it is a type of dates, which can include any type of dates'
}

for name in glossary:
    print(f"{name.title()} - {glossary[name]}")