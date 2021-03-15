"""
CP1404/CP5632 - Practical
"""

numbers = []
for i in range(5):
    number = int(input("Enter a number here: "))
    numbers.append(number)

print(f"fThe first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The biggest number is {max(numbers)}")
print(f"The average number is {sum(numbers) / sum(numbers)}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter username here: ")

if username in usernames:
    print("Access granted.")
else:
    print("Access denied.")