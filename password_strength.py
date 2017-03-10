import re
from collections import namedtuple

pattern_class = namedtuple('pattern_class', ['regexp', 'points'])

password_patterns = {
    'lower_case': pattern_class(regexp=re.compile(r'[a-zа-я]'), points=1),
    'upper_case': pattern_class(regexp=re.compile(r'[A-ZА-Я]'), points=1),
    'digits': pattern_class(regexp=re.compile(r'[0-9]'), points=1),
    'special_characters': pattern_class(regexp=re.compile(r'[\[\]{}()<>~_+-=!?;:,.@#$%&`*/|\\^\' ]'), points=2),
    'phone_number': pattern_class(regexp=re.compile(r'\+?[0-9\-()\s]{6,}'), points=-2),
    'date': pattern_class(regexp=re.compile(r'([0-9]{1,4}[./\s]?){3}'), points=-2),
    'car_number': pattern_class(regexp=re.compile(r'[a-zа-я][0-9]{3}[a-zа-я]{2}'), points=-2)
}


def is_password_top_used(password):
    """
    Check password against well-known top used passwords
    """
    with open('top_10000.txt', mode='r', encoding='utf-8') as f:
        if password in f.read():
            return True
    return False


def get_password_strength(password):
    if is_password_top_used(password):
        return 1
    strength = 1
    for pattern in password_patterns.values():
        if pattern.regexp.search(password):
            strength += pattern.points
    if len(password) >= 8:
        strength += 2
    if len(password) >= 14:
        strength += 2
    return strength


if __name__ == '__main__':
    psswd = input('Please enter your password: ')
    print('Your password is {}/10'.format(get_password_strength(psswd)))