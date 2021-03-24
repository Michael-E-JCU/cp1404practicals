"""
CP1404/CP5632 - Practical
"""

numbers = []
count = 1
number = int(input(f"Enter a number {count}: "))
numbers.append(number)
while number > 0:
    count += 1
    number = int(input(f"Enter a number {count}: "))
    numbers.append(number)

print(f"fThe first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The biggest number is {max(numbers)}")
print(f"The average number is {sum(numbers) / len(numbers)}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter username here: ")

if username in usernames:
    print("Access granted.")
else:
    print("Access denied.")
