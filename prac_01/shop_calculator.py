"""
CP1404/CP5632 - Practical
Pseudocode for shop_calculator

"""

total = 0

number = int(input("Number of items: "))

while number <= 0:
    print("Invalid number of items!")
    number = int(input("NUmber of items: "))

for i in range(number):
    item = float(input("Price of item: "))
    total += item

print(f"Total price for {number} of items is ${total:.2f}")
