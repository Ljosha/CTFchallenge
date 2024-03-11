import random

 
with open('flag.txt','r') as file:
    message = " ".join(line.rstrip() for line in file)
    print(message)
    
# Function to encode the message using hexadecimal
def hex_encode(message):
    return message.encode('utf-8').hex()

# Function to encode the message using Ceasar's cipher with a shift of 16
def caesar_cipher(message, shift=16):
    encoded = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encoded += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encoded += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encoded += char
    return encoded

# Encode the message using hexadecimal
hex_encoded = hex_encode(message)
print("Hexadecimal Encoded:", hex_encoded)

# Encode the message using Ceasar's cipher with a shift of 16
caesar_encoded = caesar_cipher(message)
print("Ceasar's Cipher Encoded:", caesar_encoded)
