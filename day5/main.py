import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = ""
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for letter in range(1, nr_letters + 1):
    password += letters[random.randint(0, len(letters) - 1)]

for number in range(1, nr_numbers + 1):
    password += numbers[random.randint(0, len(numbers) - 1)]

for symbol in range(1, nr_symbols + 1):
    password += symbols[random.randint(0, len(symbols) - 1)]

print(f"Not randomised character order: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = list(password)

for index in range(0, len(password) - 1):
    swap_index_one = random.randint(0, len(password) - 1)
    swap_index_two = random.randint(0, len(password) - 1)
    old = password[swap_index_one]
    password_list[swap_index_one], password_list[swap_index_two] = password_list[swap_index_two], password_list[swap_index_one]

password = ''.join(password_list)
print(f"Randomised character order: {password}")


