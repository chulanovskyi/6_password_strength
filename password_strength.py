import re
from urllib.request import Request, urlopen


MIN, SMALL, MEDIUM, BIG = (3, 8, 12, 15)


def get_blacklist():
    request = Request(
        'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10_million_password_list_top_1000.txt')
    with urlopen(request) as response:
        page = response.read()
        top_1000 = page.decode('utf-8').split('\n')
    return top_1000


def get_password_strength(password):
    strength = 0
    top_100 = top_1000[:100]
    if not len(password) >= MIN:
        return 'Minimum password length = 3' 
    if len(password) >= SMALL:
        strength += 1
    if len(password) >= MEDIUM:
        strength += 1
    if len(password) >= BIG:
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'\d', password):
        strength += 1
    if re.search(r'\W', password):
        strength += 1
    if password not in top_100:
        strength += 1
    if password not in top_1000:
        strength += 1
    if any(ch.isupper() for ch in password):
        strength += 1
    return strength


if __name__ == '__main__':
    print('Loading most common passwords...')
    top_1000 = get_blacklist()
    password = input('Enter password: ')
    pass_strength = get_password_strength(password)
    print('Complexity of your password is: %s' % pass_strength)
