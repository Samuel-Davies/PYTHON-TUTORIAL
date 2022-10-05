# Assignment for computer security lecturer

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ .,')
substitute = list('KCPSVMHFDBUWQNRYTJOIXELAZG .,')


original = input("Enter Plain Text here : ")
original = original.upper()


def encrypt(original):
    cipher = ''
    for letter in original:
        if letter in alphabet:
            index = alphabet.index(letter)

            cipher = str(cipher + substitute[index])
    return print(cipher)



encrypt(original)


ciphertext = input("Enter Ciphertext : ")
ciphertext.upper()

def decrypt(ciphertext):
    plaintext = ''
    for letter in ciphertext:
        if letter in substitute:
            index = substitute.index(letter)
            plaintext = str(plaintext + alphabet[index])
    return print(plaintext)


decrypt(ciphertext)