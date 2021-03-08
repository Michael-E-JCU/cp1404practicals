import random


def main():
    write_random_temps(15)
    conversion_type = "C"
    in_file = open("temps_input.txt", "r")
    out_file = open("temps_output.txt", "w")
    for lines in in_file:
        if conversion_type == "C":
            converted_temp = convert_celsius_to_fahrenheit(float(lines))
        else:
            converted_temp = convert_fahrenheit_to_celsius(float(lines))
        print(converted_temp, file=out_file)
    in_file.close()
    out_file.close()


def convert_fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def write_random_temps(amount):
    out_file = open("temps_input.txt", "w")
    for num in range(amount):
        random_number = random.uniform(-200, 200)
        print(random_number, file=out_file)
    out_file.close()


main()
