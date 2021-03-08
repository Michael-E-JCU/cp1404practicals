"""
CP1404/CP5632 - Practical
"""

finished = False
number = 0
while not finished:
    try:
        number = int(input("Enter integer: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")

print(f"Valid result is: {number}")
