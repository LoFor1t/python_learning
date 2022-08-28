class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0
        self.flavors = flavors

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

    def get_flavors(self):
        for flavor in self.flavors:
            print(flavor.title())


IceCreamStand = Restaurant('claud monet', 'european', 'chocolate', 'vanilla', 'strawberry')
IceCreamStand.get_flavors()
