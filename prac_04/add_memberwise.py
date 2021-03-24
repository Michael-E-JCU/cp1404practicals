def main():
    list1, list2 = [1, 2, 3], [4, 5, 6]
    combined = add_memberwise(list1, list2)
    print(combined)


def add_memberwise(list1, list2):
    combined = []
    count = 0
    for i in range(
            len(list1)):  # For the length of the list, it will add each list item together and append to combined
        combination = list1[count] + list2[count]
        combined.append(combination)
        count += 1  # Count for running through list items
    return combined


main()
