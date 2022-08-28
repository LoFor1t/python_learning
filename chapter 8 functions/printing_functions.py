def print_models(unprinted_designs, completed_models):
    """
    Цикл последовательно печатает каждую модель до конца списка.
    После печати каждая модель перемещается в список completed_models
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Имитация печати на 3-D принтере.
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """
     Выводит информацию о всех напечатанных моделях.
    """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(f"\t{completed_model}")