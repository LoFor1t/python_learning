from collections import OrderedDict

glossary = OrderedDict()

glossary['variable'] = 'this is a container, which can have in itself any information.'
glossary['boolean expression'] = 'this is expression, which can have only True or False'
glossary['integer'] = 'it is type of dates which can have only numbers'
glossary['string'] = 'it is type of dates which can have any symbols'
glossary['list'] = 'it is a type of dates, which can include any type of dates'

for name, meaning in glossary.items():
    print(f"{name.title()} is meaning {meaning}.")
