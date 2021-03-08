"""
CP1404/CP5632 - Practical
Pseudocode for loops
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_stars = int(input("How many stars?: "))
for stars in range(number_of_stars):
    print("*", end='')
print()

counting = 0
while counting != number_of_stars:
    for i in range(counting + 1):
        print("*", end='')
    print()
    counting += 1
