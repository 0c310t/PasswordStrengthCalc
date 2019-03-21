import math
import decimal

def passBits(password, alphabet, specialChar, numChar):

    count = 0

    for char in password:
        if char in alphabet:
            count = count + math.log(52, 2)
        elif char in specialChar:
            count = count + math.log(33, 2)
        elif char in numChar:
            count = count + math.log(10, 2)

    return count

def charCount(password, alphabet, specialChar, numChar):

    charCounter = [0, 0, 0]

    for char in password:
        if char in alphabet:
            charCounter[0] = charCounter[0] + 1
        elif char in specialChar:
            charCounter[1] = charCounter[1] + 1
        elif char in numChar:
            charCounter[2] = charCounter[2] + 1

    return charCounter

loop = "y"

while loop == "y":

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    specialChar = [' ', '!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '\\', "'"]
    numChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    password = str(input("\nPlease enter a password to be tested:\n"))
    password = list(password)

    entropyBits = math.ceil(passBits(password, alphabet, specialChar, numChar))
    charCounter = charCount(password, alphabet, specialChar, numChar)

    
    print("\nYour password is", len(password), "characters long.")
    print("There are", charCounter[0], "letters,", charCounter[1], "special characters, and", charCounter[2], "numbers.")
    if entropyBits <= 30:
        print("Your password has", entropyBits, "bits of entropy.\nThis is very weak, you should consider using letters, numbers, and special characters and making your password longer.")
    elif entropyBits in range(31, 40):
        print("Your password has", entropyBits, "bits of entropy.\nThis is an okay password, but still relatively weak.")
    elif entropyBits in range(41, 60):
        print("Your password has", entropyBits, "bits of entropy.\nThis is a relatively strong password. It should be okay for non-financial logins.")
    elif entropyBits in range(61, 127):
        print("Your password has", entropyBits, "bits of entropy.\nThis is a very strong password, and should be good for any purpose including financial logins.")
    elif entropyBits >= 128:
        print("Your password has", entropyBits, "bits of entropy.\nThis password could be considered overkill. If you can remember it, you could use it for any purpose!")
        
    loop = input("\nWould you like to test another password? (y/n): ")
