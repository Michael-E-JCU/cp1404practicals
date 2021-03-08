"""
CP1404/CP5632 - Practical
Pseudocode for sales_bonus


Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():
    bonus = 0
    sales = float(input("Enter sales: $"))
    while sales >= 0:
        if sales < 1000:
            bonus = sales * 1.10
        elif sales >= 1000:
            bonus = sales * 1.15
        print(f"Your bonus is ${bonus:.0f} which is a ${(bonus - sales):.0f} bonus.")
        sales = float(input("Enter sales: $"))
    else:
        quit()


main()
