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
    if score < 0:
        return "Invalid score"
    elif score >= 50 and score < 90:
        return "Passable"
    elif score >= 90 and score <= 100:
        return "Excellent"
    elif score > 100:
        return "Invalid score"
    else:
        return "Bad"


def generate_random_result():
    result = determine_result(random.randint(0, 100))
    return result


main()
