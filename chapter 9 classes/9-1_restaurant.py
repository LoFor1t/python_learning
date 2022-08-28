class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant {self.name.title()} have a {self.cuisine} cuisine.")

    def open_restaurant(self):
        print(f"{self.name.title()} is open!")


my_restaurant = Restaurant('claud monet', 'european')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
