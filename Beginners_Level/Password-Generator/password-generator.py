import random
import string
import secrets

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
selection_list = letters + digits + special_chars

password_len = int(input("Enter length of password: "))

password = ""

for i in range(password_len):
    password += "".join(secrets.choice(selection_list))

print(password)
