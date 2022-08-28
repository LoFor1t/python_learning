number = int(input("Please write a number, which you want to verify: "))

if number % 10 == 0:
    print(f"{number} is multiple of 10.")
else:
    print(f"{number} isn't multiple of 10.")
