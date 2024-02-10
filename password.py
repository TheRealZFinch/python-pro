import random

letters = "abcdefghijklmnopqrstuvwxyz"
letters_capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "01234567890"
symbols = "!#$%&'()*+,-./"

chars = letters + letters_capital + nums + symbols

length = int(input("Wpisz długość hasła: ")) - 3

password = ""

for x in range(length):
    password = password + random.choice(chars)

password = password + random.choice(symbols)
for x in range(3):
    password = password + random.choice(nums)

password = ''.join(random.sample(password, len(password)-1))

print(password)