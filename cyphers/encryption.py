# monoalphabetic cip
import string
#plaintext = 'the quick brown fox jumps over the lazy dog'
plaintext = input("Enter Plaintext here: ")
key = "KCPSVMHFDBUWQNRYTJOIXELAZG"
cipher = ''

for letter in plaintext:
    if letter in string.ascii_lowercase:
        index = ord(letter) - ord('a')
        cipher = cipher + key[index]
    else:
        cipher = cipher + letter

print("plaintext: " + plaintext)
print("Ciphertext: " + cipher)