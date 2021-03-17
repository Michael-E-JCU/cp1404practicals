"""
CP1404/CP5632 - Practical
"Quick Pick" Lottery Ticket Generator
"""
import random

NUMBER_OF_CYCLES = 6


def main():
    number_of_picks = int(input("How many quick picks? "))
    LISTS = [generate_list_of_6_random_numbers() for i in range(number_of_picks)]
    for number_list in LISTS:
        for i in number_list:
            print(f"{i:2}", end=" ")
        print("")


def generate_list_of_6_random_numbers():
    numbers_list = []
    for i in range(NUMBER_OF_CYCLES):
        number = random.randint(1, 45)
        while number in numbers_list:
            number = random.randint(1, 45)
        numbers_list.append(number)
        numbers_list.sort()
    return numbers_list


main()
