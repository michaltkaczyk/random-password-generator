import random
import string

def generate_password(length, **cases):
    password_dough = []

    positive_cases = {key: value for key, value in cases.items() if value}
    
    if len(positive_cases) == 0:
        raise Exception("You should include at least one type of characters.")

    # Chosing equal number of elements from each to assure equal expected share of characters of different size
    for case in positive_cases.keys():
        if case == "lowercase":
            password_dough += random.choices(string.ascii_lowercase, k = length)
        if case == "uppercase":
            password_dough += random.choices(string.ascii_uppercase, k = length)
        if case == "numbers":
            password_dough += random.choices(string.digits, k = length)
        if case == "symbols":
            password_dough += random.choices(string.punctuation, k = length)

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
    length = input("How long should the password be: ")
    try:
        length = int(length)
    except:
        print("Provided password length should be an integer.")
        return None

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
