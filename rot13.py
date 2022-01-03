def rot13(message):
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    answer = []
    for character in message:
        if character in upper_letters:
            new_letter_index = upper_letters.find(character) + 13
            new_letter = upper_letters[new_letter_index]
            print(new_letter)
            answer.append(new_letter)

        elif character in lower_letters:
            new_letter_index = lower_letters.find(character) + 13
            new_letter = lower_letters[new_letter_index]
            print(new_letter)
            answer.append(new_letter)
        
        else:
            print(character)
            answer.append(character)

    return ''.join(answer)

rot13("Test!")

#Liked solutions
import string
def rot13(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    outputMessage = ""
    for letter in message:
        if letter in alpha.lower():
            outputMessage += alpha[(alpha.lower().index(letter) +13) % 26].lower()
        elif letter in alpha:
            outputMessage += alpha[(alpha.index(letter) +13) % 26]
        else:
            outputMessage += letter
    return outputMessage

#% finds 