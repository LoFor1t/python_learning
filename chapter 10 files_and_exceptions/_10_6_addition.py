first_number = input("First number: ")
second_number = input("Second number: ")
try:
    result = int(first_number) + int(second_number)
except ValueError:
    print("You enter not a number!")
else:
    print(result)
