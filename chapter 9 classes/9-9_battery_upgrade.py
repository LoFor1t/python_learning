class Car:
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, miles):
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")


class Battery:
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size=70):
        """Инициализируем атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has {self.battery_size}-kWh battery.")

    def get_range(self):
        range_distance = 0
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 70:
            range_distance = 240
        elif self.battery_size == 85:
            range_distance = 270

        message = f"This car can go approximately {range_distance} miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса родителя.
        Затем инициализирует атрибуты, специфические для электромобиля.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    @staticmethod
    def fill_gas_tank():
        """У электромобилей нет бензобака."""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.fill_gas_tank()
# my_tesla.battery.get_range()
