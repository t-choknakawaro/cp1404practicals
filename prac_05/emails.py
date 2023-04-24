emails = {}
while True:
    email = input("Enter email: ")
    if not email:
        break
    name = email.split('@')[0].replace('.', ' ').title()
    check = input(f"Is your name {name}? (Y/n) ").lower()
    if check and check[0] == 'n':
        name = input("Enter name: ")
    emails[email] = name

for email, name in emails.items():
    print(f"{name} ({email})")

