prompt = "\nPlease enter a addition: "
prompt += "\n(To stop - write 'quit') "

while True:
    add = input(prompt)

    if add == 'quit':
        break
    else:
        print(add.title())
