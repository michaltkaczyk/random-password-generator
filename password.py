import random
import string


def generate_random_letter():
    return random.choice(string.ascii_lowercase)


def generate_password(length):
    password = ""

    for character in range(length):
        password += generate_random_letter()

    return password


def main():
    length = int(input("How long should the password be: "))
    password = generate_password(length)
    print(password)


if __name__ == '__main__':
    main()
