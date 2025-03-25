#####################################################################################
#                                  PROJECT Nº1                                      #
#                              PASSWORD GENERATOR                                   #
#####################################################################################
import random as rdm
import string as str
import pyperclip as py # It is necessary to install pyperclip: pip install pyperclip

def passwordGenerator(length, upper, number, symbol):
    caracters = str.ascii_lowercase #abcdefghijklmnopqrstuvwxyz
    if upper:
        caracters += str.ascii_uppercase #ABCDEFGHIJKLMNOPQRSTUVWXYZ
    if number:
        caracters += str.digits #0123456789
    if symbol:
        caracters += str.punctuation #!”#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    password = ''.join(rdm.choice(caracters) for _ in range(length))
    py.copy(password)
    print("The new password " + password + " was copied to your clipboard! Have a great day.")

try:
    length = int(input("Please, select length of password: "))
except:
    print("Your input length was not an integer. Length will be set to 10.")
    length = 10
finally:
    upper = input("Please, choose if you wish to have uppercase letters in your password (Y/N): ").lower() == 'y'
    number = input("Please, choose if you wish to have numbers in your password (Y/N): ").lower() == 'y'
    symbol = input("Please, choose if you wish to have symbols in your password (Y/N): ").lower() == 'y'
    passwordGenerator(length, upper, number, symbol)

# Brought to you by RDMP18