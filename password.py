import random
import string


def generate_password(length, **cases):
    password_dough = []

    positive_cases = {key: value for key, value in cases.items() if value}

    for case in positive_cases.keys():
        if case == "lowercase":
            for character in range(length):
                password_dough += random.choice(string.ascii_lowercase)
        if case == "uppercase":
            for character in range(length):
                password_dough += random.choice(string.ascii_uppercase)
        if case == "numbers":
            for character in range(length):
                password_dough += random.choice(string.digits)
        if case == "symbols":
            for character in range(length):
                password_dough += random.choice(string.punctuation)

    random.shuffle(password_dough)
    password = "".join(password_dough[:length])

    return password


def ask(mode_name):
    answer = input("Should " + mode_name + " be skipped [Y]: ").upper()

    if answer == "Y":
        use_mode = False
    else:
        use_mode = True

    return use_mode


def main():
    length = int(input("How long should the password be: "))
    lowercase = ask("lowercase characters")
    uppercase = ask("uppercase characters")
    numbers = ask("numbers")
    symbols = ask("symbols")
    password = generate_password(length, lowercase=lowercase, uppercase=uppercase, numbers=numbers, symbols=symbols)
    print(password)


if __name__ == '__main__':
    main()
