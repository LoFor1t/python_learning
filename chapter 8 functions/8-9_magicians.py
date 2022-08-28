def show_magicians(magicians):
    print("List of magicians: ")
    for magician in magicians:
        print(f"\t{magician.title()}")


list_magicians = ['Carl', 'Ella', 'Kate']
show_magicians(list_magicians)
