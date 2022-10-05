import string
key = "KCPSVMHFDBUWQNRYTJOIXELAZG"
cipher = input('Enter cipher text: ')

plaintext = ''

for letter in cipher:
    if letter in string.ascii_uppercase:
        index = key.find(letter)
        plaintext = plaintext + chr(index + ord('a'))
    else:
        plaintext = plaintext + letter

print("Ciphertext: " + cipher)
print("plaintext: " + plaintext)