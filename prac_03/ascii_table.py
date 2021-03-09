MAX_NUMBER = 127
MIN_NUMBER = 33


def main():
    char = input("Enter character here: ")
    char_code = ord(char)
    print(f"The ASCII code for {char} is {char_code}")
    number = int(input(f"Enter a number between {MIN_NUMBER} and {MAX_NUMBER}: "))
    while not validate_ascci_code(number):
        print(f"Invalid! Must be between {MIN_NUMBER} and {MAX_NUMBER}!")
        number = int(input(f"Enter a number between {MIN_NUMBER} and {MAX_NUMBER}: "))
    print(f"The character for {number} is {chr(number)}")
    count = MIN_NUMBER
    while count <= MAX_NUMBER:
        print("{0:3} {1}".format(count, chr(count)))
        count += 1


def validate_ascci_code(number):
    if number > MAX_NUMBER or number < MIN_NUMBER:
        return False
    return True


main()
