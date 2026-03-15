import random
import string

def generate_password():
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Please enter a number")
        return

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)


def check_strength():
    password = input("Enter password to check: ")

    if len(password) < 6:
        print("Strength: Weak")
    elif len(password) < 10:
        print("Strength: Medium")
    else:
        print("Strength: Strong")


while True:
    print("\n1. Generate Password")
    print("2. Check Password Strength")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_password()

    elif choice == "2":
        check_strength()

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again.")