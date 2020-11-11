# Project for day 5
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
    'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

#total_nr= nr_letters+nr_symbols+nr_numbers
while nr_letters > 0 & nr_symbols>0 & nr_numbers >0:
    if random.randint(1,3) ==1: #letters
        password.append(random.choice(letters))
        nr_letters -=1
    if random.randint(1,3) ==2: #symbols
        password.append(random.choice(symbols))
        nr_symbols -=1
    if random.randint(1,3) ==3: #numbers
        password.append(random.choice(numbers))
        nr_numbers -=1
        

passString = ''.join([str(elem) for elem in password]) 
print(f"Here is your password: {passString}")
