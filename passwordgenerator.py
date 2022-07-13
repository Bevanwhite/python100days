# password Generator Project
import random
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# option01
ra_letters = []
for i in range(0, nr_letters):
    ra_letters += random.choice(letter)
ra_symbols = []
for i in range(0, nr_symbols):
    ra_symbols += random.choice(symbols)
ra_numbers = []
for i in range(0, nr_numbers):
    ra_numbers += random.choice(numbers)

ra_sequances = ra_letters + ra_numbers + ra_symbols
print(ra_sequances)
random.shuffle(ra_sequances)
password_you_get = ""
for i in ra_sequances:
    password_you_get += i

print(f"Here is your password: {password_you_get}")
# option 02
ra_letters = random.choices(letter,  k=nr_letters)
ra_symbols = random.choices(numbers, k=nr_numbers)
ra_numbers = random.choices(symbols, k=nr_symbols)
ra_sequance = ra_letters + ra_numbers + ra_symbols
print(ra_letters,ra_numbers,ra_symbols)

random.shuffle(ra_sequance)
print(ra_sequance)
your_password = ""
for i in ra_sequance:
    your_password += str(i)
print(f"Here is your password: {your_password}")



