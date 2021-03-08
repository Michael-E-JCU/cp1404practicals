MIN_LEN = 10


def main():
    password = get_password()
    while not get_valid_password(password):
        print("Invalid paassword length! Must be at least 10 characters.")
        password = get_password()
    get_asterisks(password)


def get_asterisks(password):
    for l in password:
        print("*", end="")


def get_password():
    password = input("Enter password here: ")
    return password


def get_valid_password(password):
    if len(password) < MIN_LEN:
        return False
    return True


main()
