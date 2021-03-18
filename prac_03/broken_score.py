"""
CP1404/CP5632 - Practical
Pseudocode for debugging
"""
import random


def main():
        score = float(input("Enter score: "))
        result = determine_result(score)
        print(result)
        random_result = generate_random_result()
        print(f"Random result: {random_result}")


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def generate_random_result():
    result = determine_result(random.randint(0, 100))
    return result


main()
