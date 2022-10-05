
alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ .,')
plain = ''
cipher = ''

plaintext = input("Enter plaintext ").upper()

for letter in plaintext:
    if letter in alphabet:
        pos = alphabet.index(letter)
        shift = pos % 10
        encryption = pos + shift
        if encryption > 25:
            encryption = encryption-26

        cipher = str(cipher + alphabet[encryption])

print(cipher)

ciphertext = input("Enter the ciphertext: ").upper()
for i in ciphertext:
    if i in alphabet:
        position = alphabet.index(i)
        # print(position)
        shift_value = position % 10

        decryption = position-shift_value
        plain =str(plain + alphabet[decryption])

print(plain)       












        