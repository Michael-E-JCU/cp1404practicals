"""
CP1404/CP5632 Practical

"""


def main():
    emails = {"michael.excell@my.jcu.edu.au": "Michael Excell"}
    input_email = input("Email: ").lower()
    if input_email in emails:
        confirm_name = input(f"Is your name {emails.get(input_email)} (Y/N): ").lower()
        if confirm_name == "n":
            name = input("Enter name here: ")
            emails[input_email[0]].append(name)
    print(emails)

main()
