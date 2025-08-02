# password_generator.py

import random
import string


print("****** PASSWORD GENERATOR ******\n")

while True:  
    while True:
        length_input = input("\nEnter the desired password length: ")
        if length_input.isdigit():
            length = int(length_input)
            if length < 4:
                print("Password should be at least 4 characters long for better security.\n")
            else:
                break
        else:
            print("Please enter a valid number.\n")
        
    print("\nChoose what to include in the password:")

    include_upper = input("\nInclude uppercase letters? (y/n): ").lower() == 'y'
    include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'


    characters = ''
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if characters == '':
        print("\nNo character types selected. Please run the program again.")
    else:
        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"\nGenerated Password: {password}\n")

    while True:
        again = input("Do you want to generate another password? (y/n): ").lower()
        if again in ['y', 'n']:    
            break
        print("\nInvalid input! Please enter 'y' or 'n'.")

    if again == 'n':
        print("\nThanks for using the password generator.Goodbye!\n")
        break
