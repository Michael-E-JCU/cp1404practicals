import random


def main():
    number = int(input("Number of scores: "))
    out_file = open("results.txt", "w")
    for x in range(number):
        score = generate_random_score()
        result = determine_result(score)
        print(f"{score} is {result}", file=out_file)
    out_file.close()


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


def generate_random_score():
    score = random.randint(0, 100)
    return score


main()

