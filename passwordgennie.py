import random

print("Password Gennie")

PASS_AMOUNT = input("How many passwords would you like?")
PASS_AMOUNT = int(PASS_AMOUNT)
CHAR_AMOUNT = input("How long would you like your Password? ")
CHAR_AMOUNT = int(CHAR_AMOUNT)

chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
print("Here are your passwords!!")
# make sure range is correct

for p in range(0, PASS_AMOUNT):
    pwd = ''
    for c in range(0, CHAR_AMOUNT):
        pwd += random.choice(chars)
    print(pwd)


