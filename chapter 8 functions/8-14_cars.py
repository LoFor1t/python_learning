def make_car(brand, model, **information):
    car = {}
    car['brand'] = brand
    car['model'] = model
    for key, value in information.items():
        car[key] = value
    return car


car = make_car('subaru', 'outback',
               color='blue',
               tow_package=True)
print(car)
