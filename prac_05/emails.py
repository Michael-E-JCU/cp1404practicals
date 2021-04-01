"""
CP1404/CP5632 Practical

"""


def main():
    emails = {}
    email = input("Email: ").lower()
    while email != "":
        split_email = email.split("@")
        name = split_email[0].title().replace(".", " ")
        emails.update({email: name})
        confirm_name = input(f"Is your name {emails.get(email)}? (Y/N): ").lower()
        while confirm_name != "n" and confirm_name != "y":
            print("INVALID OPTION!")
            print(confirm_name)
            confirm_name = input(f"Is your name {emails.get(email)}? (Y/N): ").lower()
        if confirm_name == "n":
            new_name = input("Name: ").title()
            emails[email] = new_name
        email = input("Email: ").lower()
    for email in emails:
        print(f"{emails.get(email)} ({email})")


main()
