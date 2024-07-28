
# Encryption program

import random
import string

#Encrypt
def encryption():

    chars = " "+string.punctuation+string.digits+string.ascii_letters
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)

    plain_text = input("Enter a messasge to encrypt: ")
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]
    
    print(f"Original message: {plain_text}")
    print(f"Encrypted message: {cipher_text}")

encryption()

# Decrypt Program
"""
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message: {cipher_text}")
print(f"Original message: {plain_text}")
"""