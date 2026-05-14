import re

with open("input.txt", "r") as file:
    data = file.read()

emails = re.findall(r'\S+@\S+', data)

with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email addresses extracted successfully!")