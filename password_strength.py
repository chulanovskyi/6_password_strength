import re
import os
import sys

TOP_50_PASSWORDS = ['123456', 'password', '12345678', 'qwerty', '123456789',
                     '12345', '1234', '111111', '1234567', 'dragon',
                     '123123', 'baseball', 'abc123', 'football', 'monkey',
                     'letmein', '696969', 'shadow', 'master', '666666',
                     'qwertyuiop', '123321', 'mustang', '1234567890', 'michael',
                     '654321', 'pussy', 'superman', '1qaz2wsx', '7777777',
                     'fuckyou', '121212', '000000', 'qazwsx', '123qwe',
                     'killer', 'trustno1', 'jordan', 'jennifer', 'zxcvbnm',
                     'asdfgh', 'hunter', 'buster', 'soccer', 'harley',
                     'batman', 'andrew', 'tigger', 'sunshine', 'iloveyou']


def load_file(file_path):
    with open(file_path) as text_file:
        return text_file.read()


def get_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'\d', password):
        strength += 1
    if re.search(r'\W', password):
        strength += 1
    if password not in TOP_50_PASSWORDS:
        strength += 1
    return strength

if __name__ == '__main__':
    password = input('Enter password: ')
    print(get_password_strength(password))
    
