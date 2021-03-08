INVALID_PASSWORD = "Invalid password!"
SPECIAL_CHARACTES = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
MAX_LENGTH = 15
MIN_LENGTH = 5


def main():
    print("""
    Please enter a valid password
    Your password must be between MIN_LENGTH and MAX_LENGTH characters, and contain:
        1 or more uppercase characters
        1 or more lowercase characters
        1 or more numbers
        and 1 or more special characters:  !@#$%^&*()_-=+`~,./'[]<>?{}|\
    """)
    password = input("Password: ")
    while not validate_password(password):
        print("Invalid password!")
        password = input("Password: ")
    print(f"Your {len(password)} character password is vaiid: {password}")


def validate_password(password):
    """Determine if the password is valid"""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_special = 0
    count_number = 0

    for char in password:
        if char.isdigit():
            count_number += 1
        elif char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char in SPECIAL_CHARACTES:
            count_special += 1
    if count_special == 0 or count_upper == 0 or count_number == 0 or count_lower == 0:
        return False

    return True


main()
