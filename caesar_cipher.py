def caesar_cipher(message,key):
    result = ''
for character in message:
    if character.isalpha():
        if character.isupper():
            start = ord('A')
        else:
            start = ord('a')
        c = ord(character) - start
        result+= chr((c + key) % 26 + start)
    else:
        result += character
    return result

message = input('Enter a message to encrypt: ')
key = int(input('Please enter the secret key (between 1 and 25): '))
if key < 1 or key > 25:
    print('Error: key must be between 1 and 25')
    exit()

cipher = caesar_cipher(message, key)
print(cipher)
