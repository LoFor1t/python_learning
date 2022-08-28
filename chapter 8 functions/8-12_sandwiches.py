def making_sandwich(*toppings):
    print(f"\nYou add to your sandwich: ")
    for topping in toppings:
        print(f"\t{topping}")


making_sandwich('cheese', 'sausages', 'meet')
