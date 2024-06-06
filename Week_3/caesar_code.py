alphabet = list("abcdefghijklmnopqrstuvwxyz")

def code_message(alphabet, key, text):
    coded_message = ""
    for letter in text:
        if letter in alphabet:
            current_index = alphabet.index(letter)
            caesar_index = current_index + key
            if caesar_index > 26:
                caesar_index -= 26
            coded_message += alphabet[caesar_index]
        else:
            coded_message += letter
    return coded_message



def decode_message(alphabet, key, text):
    decoded_message = ""
    for letter in text:
        if letter in alphabet:
            caesar_index = alphabet.index(letter)
            original_index = caesar_index - key
            if original_index < 0:
                original_index += 26
            decoded_message += alphabet[caesar_index]
        else:
            decoded_message += letter
    return decoded_message




print("choose option")
print("1. Code message")
print("2. Decode message")
option = int(input())
text = input("Enter message: \n")


if option == 1:
    code_message(alphabet, 6, text)
elif option == 2:
    decode_message(alphabet, 5, text)
