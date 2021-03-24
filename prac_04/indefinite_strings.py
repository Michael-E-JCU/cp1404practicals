strings = []

response = input("Entere string here: ")
strings.append(response)
while response != "":
    response = input("Entere string here: ")
    strings.append(response)
total = 0
for string in strings:
    count = strings.count(string)
    if count > 1:
        print(string, end=' ')
        total += 1

if total == 0:
    print("No repeated strings entered")
