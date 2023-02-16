MIN_PASSWORD_LENGTH = 4
MAX_PASSWORD_LENGTH = 64

import random
import string

def generate_password(length, **cases):
    password_starter = []
    password_dough = []
    
    positive_cases = {key: value for key, value in cases.items() if value}
    
    if len(positive_cases) == 0:
        print("You should include at least one type of characters.")
        exit()

    # Chosing equal number of elements from each to assure equal expected share of characters of different type
    # Adding a single element of each type to assure that the password contains at least one of each type of characters
    for case in positive_cases.keys():
        if case == "lowercase":
            password_dough += random.choices(string.ascii_lowercase, k = length)
            password_starter += random.choice(string.ascii_lowercase)
        if case == "uppercase":
            password_dough += random.choices(string.ascii_uppercase, k = length)
            password_starter += random.choice(string.ascii_uppercase)
        if case == "numbers":
            password_dough += random.choices(string.digits, k = length)
            password_starter += random.choice(string.digits)
        if case == "symbols":
            password_dough += random.choices(string.punctuation, k = length)
            password_starter += random.choice(string.punctuation)

    password_elements = password_starter + random.choices(password_dough, k = length - len(password_starter))
    random.shuffle(password_elements)
    password = "".join(password_elements)

    return password

def ask(mode_name):
    answer = input("Should " + mode_name + " be skipped [Y]: ").upper()

    if answer == "Y":
        use_mode = False
    else:
        use_mode = True

    return use_mode

def ask_length():
    length = input("How long should the password be: ")

    try:
        length = int(length)
    except ValueError:
        print("Provided password length should be an integer.")
        exit()

    if length < MIN_PASSWORD_LENGTH:
        print("Provided password length should be at least {} characters long.".format(MIN_PASSWORD_LENGTH))
        exit()

    if length > MAX_PASSWORD_LENGTH:
        print("Provided password length can't be longer than {} characters.".format(MAX_PASSWORD_LENGTH))
        exit()

    return length

def main():
    length = ask_length()

    lowercase = ask("lowercase characters")
    uppercase = ask("uppercase characters")
    numbers = ask("numbers")
    symbols = ask("symbols")

    password = generate_password(
        length,
        lowercase = lowercase,
        uppercase = uppercase,
        numbers = numbers,
        symbols = symbols)
    
    print(password)

if __name__ == '__main__':
    main()
