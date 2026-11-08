
import string
import random

while True:
    characters = ""
    try:
        length = int(input("HOW MANY CHARACTERS DOES THE PASSWORD SHOULD CONTAIN:\n"))
        count = int(input("Enter the number of passwords to be generated:\n"))

        letters = input("Include letters yes/no: ").lower()
        numbers = input("Include numbers yes/no: ").lower()
        symbols = input("Include symbols yes/no: ").lower()

        if letters == "yes":
            characters += string.ascii_letters

        if numbers == "yes":
            characters += string.digits

        if symbols == "yes":
            characters += string.punctuation

        if characters == "":
            print("Select at least one character type!")
        else:
            if length > 0 and count > 0:
                break
            else:
                print("Enter valid input!")

    except ValueError:
        print("Enter valid input!")


for i in range(count):
    password = ""
    for j in range(length):
        password += random.choice(characters)

    if count == 1:
        print("Generated password:", password)
    else:
        print("Generated password:", i+1, ":", password)
