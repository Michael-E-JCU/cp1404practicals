"""
CP1404/CP5632 Practical

"""


def main():
    emails = {}
    input_email = input("Email: ").lower()
    while input_email != "":
        split_email = input_email.split("@")
        name = split_email[0].title().replace(".", " ")
        emails.update({input_email: name})
        confirm_name = input(f"Is your name {emails.get(input_email)}? (Y/N): ").lower()
        if confirm_name == "n":
            confirm_name = input("Name: ").title()
            emails[input_email] = confirm_name
        input_email = input("Email: ").lower()
    for email in emails:
        print(f"{emails.get(email)} ({email})")

main()
