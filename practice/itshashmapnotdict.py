phonebook = {
    "nishant": "8767879213",
    "rajesh": "9929018238"
}

while True:
    op = input("Select a/d/v/e: ")
    if op == 'a':
        name = input("Enter name: ")
        number = input("Enter number: ")

        phonebook.update({ name: number })

    if op == 'd':
        name = input("Enter name: ")
        if name in phonebook.keys():
            phonebook.pop(name)

    if op == 'v':
        print("Name\tPhone")
        for (name, number) in tuple(phonebook.items()):
            print(f"{name}\t{number}")

    if op == 'e':
        break