alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ .,')
substitute = list('KCPSVMHFDBUWQNRYTJOIXELAZG .,')



ciphertext = input("Enter Ciphertext : ")
def decrypt(ciphertext):
    plaintext = ''
    for letter in ciphertext:
        if letter in substitute:
            index = substitute.index(letter)
            plaintext = str(plaintext + alphabet[index])
    return print(plaintext)
#print("Plaintext : " + decrypt(ciphertext))

decrypt(ciphertext)