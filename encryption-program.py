# Encryption Program
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()
random.shuffle(key)

# ENCRYPT
plain_text = input("Enter the text to be encrypted: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# DECRYPT
cipher_text_input = input("Enter the text to be decrypted: ")
plain_text = ""

for letter in cipher_text_input:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message: {cipher_text_input}")
print(f"Decrypted message: {plain_text}")