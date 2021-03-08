name = str(input("Enter name here: "))
out_file = open("data.txt", "w")
print(name, file=out_file)
out_file.close()
in_file = open("data.txt", "r")
name = in_file.read()
print(f"Your name is {name}")
in_file.close()
in_file = open("numbers.txt", "r")
number_1 = in_file.readline()
number_2 = in_file.readline()
in_file.close()
total = number_1 + number_2
print(total)
in_file = open("numbers.txt", "r")
total = 0
for lines in in_file:
    number = int(lines)
    total += number
print(total)
in_file.close()
