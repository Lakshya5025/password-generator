#Password Generator Project
from binascii import a2b_base64
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# #Eazy Level - Order not randomised:
# passw=""
# for charactor in range(1,nr_letters+1):
#     passw+=random.choice(letters)
# for charactor in range(1,nr_symbols+1):
#     passw+=random.choice(numbers)
# for charactor in range(1,nr_symbols+1):
#     passw+=random.choice(symbols)
# print(passw)


#Hard Level - Order of characters randomised:
password=[]
for charactor in range(1,nr_letters+1):
    password.append(random.choice(letters))
for charactor in range(1,nr_numbers+1):
    password.append(random.choice(numbers))
for charactor in range(1,nr_symbols+1):
    password.append(random.choice(symbols))
random.shuffle(password)
space=""
for chara in password:
    space+=chara
print(f"Your strong password is : {space}")
