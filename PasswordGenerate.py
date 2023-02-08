import secrets
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
password = letters + numbers + symbols
pwd_length = int(input(f"How long do you want the password?\n"))

pwd = ""

for i in range(pwd_length):
    pwd += ''.join(secrets.choice(password))

print(pwd)

