prompt = "\nSay your age: "
prompt += "\n(To stop program, write 'quit') "

while True:
    age = input(prompt)

    if age == 'quit':
        exit()
    age = int(age)
    if age < 3:
        print("Ticket is free.")
    elif age < 12:
        print("Ticket costs - $10.")
    else:
        print("Ticket costs - $15.")
