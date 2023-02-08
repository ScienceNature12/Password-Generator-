import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

print("Welcome to the password generator!")
random_letters = int(input(f"How many letters do you want?\n"))
random_symbols = int(input(f"How many symbols do you want?\n"))
random_numbers = int(input(f"How many numbers do you want?\n"))

passwords = []

for char in range(1, random_letters + 1):
    passwords.append(random.choice(letters))

for char in range(1, random_symbols + 1):
    passwords.append(random.choice(symbols))

for char in range(1, random_numbers + 1):
    passwords.append(random.choice(numbers))

random.shuffle(passwords)
password = ""
for char in passwords:
    password += char
print(f"Your Password is: {password}")

