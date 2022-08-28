def make_great(magicians, great_magicians):
    while magicians:
        magician = magicians.pop()
        great_magicians.append(f"Great {magician}")


def show_magicians(magicians):
    print("List of magicians: ")
    for magician in magicians:
        print(f"\t{magician.title()}")


list_magicians = ['Carl', 'Ella', 'Kate']
great_magicians = []
make_great(list_magicians[:], great_magicians)
show_magicians(list_magicians)
show_magicians(great_magicians)