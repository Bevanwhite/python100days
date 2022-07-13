# password Generator Project
import random
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

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



