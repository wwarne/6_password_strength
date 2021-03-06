import re
import os.path
from collections import namedtuple
from getpass import getpass

Pattern = namedtuple('pattern_class', ['regexp', 'points'])

PASSWORD_PATTERNS = {
    'lower_case': Pattern(regexp=re.compile(r'[a-zа-я]'), points=1),
    'upper_case': Pattern(regexp=re.compile(r'[A-ZА-Я]'), points=1),
    'digits': Pattern(regexp=re.compile(r'[0-9]'), points=1),
    'special_characters': Pattern(regexp=re.compile(r'[\[\]{}()<>~_+-=!?;:,.@#$%&`*/|\\^\' ]'), points=2),
    'phone_number': Pattern(regexp=re.compile(r'\+?[0-9\-()\s]{6,}'), points=-2),
    'date': Pattern(regexp=re.compile(r'([0-9]{1,4}[./\s]?){3}'), points=-2),
    'car_number': Pattern(regexp=re.compile(r'[a-zа-я][0-9]{3}[a-zа-я]{2}'), points=-2),
    'len_>=_8': Pattern(regexp=re.compile(r'.{8,}'), points=2),
    'len_>=_14': Pattern(regexp=re.compile(r'.{14,}'), points=2)
}
BLACKLIST_FILENAME = 'top.txt'


def is_blacklist_available():
    return os.path.isfile(BLACKLIST_FILENAME)


def is_password_top_used(password):
    if is_blacklist_available():
        with open(BLACKLIST_FILENAME, mode='r', encoding='utf-8') as f:
            return password in f.read()
    return False


def get_password_strength(password):
    if is_password_top_used(password):
        return 1
    strength = 1
    for pattern in PASSWORD_PATTERNS.values():
        if pattern.regexp.search(password):
            strength += pattern.points
    return strength


if __name__ == '__main__':
    if not is_blacklist_available():
        print('[INFO] For a more accurate score provide a file with top-used passwords.')
    psswd = getpass('Please enter your password: ')
    print('Your password is {}/10'.format(get_password_strength(psswd)))
