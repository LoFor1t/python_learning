class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant {self.name.title()} have a {self.cuisine} cuisine.")

    def open_restaurant(self):
        print(f"{self.name.title()} is open!")

    def set_number_served(self, people):
        if people >= 0:
            self.number_served = people
        else:
            print("You can't serve a negative amount.")

    def increment_number_served(self, people):
        if people >= 0:
            self.number_served += people
        else:
            print("You can't make amount of visitors less.")


my_restaurant = Restaurant('claud monet', 'european')
print(my_restaurant.number_served)

my_restaurant.number_served = 100
print(my_restaurant.number_served)

my_restaurant.set_number_served(-1)
print(my_restaurant.number_served)

my_restaurant.set_number_served(10)
print(my_restaurant.number_served)

my_restaurant.increment_number_served(-10)
print(my_restaurant.number_served)

my_restaurant.increment_number_served(111)
print(my_restaurant.number_served)
