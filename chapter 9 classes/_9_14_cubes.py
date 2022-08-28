from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        number = randint(1, self.sides)
        print(number)


cube6 = Die()
cube6.roll_die()
cube6.roll_die()
cube6.roll_die()
cube6.roll_die()
cube6.roll_die()
cube6.roll_die()
cube6.roll_die()
cube6.roll_die()
cube6.roll_die()
cube6.roll_die()
print('\n')

cube10 = Die(10)
cube10.roll_die()
cube10.roll_die()
cube10.roll_die()
cube10.roll_die()
cube10.roll_die()
cube10.roll_die()
cube10.roll_die()
cube10.roll_die()
cube10.roll_die()
cube10.roll_die()
print('\n')

cube20 = Die(20)
cube20.roll_die()
cube20.roll_die()
cube20.roll_die()
cube20.roll_die()
cube20.roll_die()
cube20.roll_die()
cube20.roll_die()
cube20.roll_die()
cube20.roll_die()
cube20.roll_die()
