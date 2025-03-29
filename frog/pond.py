import random
import string

def xor(var, key):
    return bytes(a ^ b for a, b in zip(var, key))

def rand_string(length, upper=True, lower=True, number=True, special=True):
    if not ( upper or lower or number or special):
        raise NameError('At least one characterset has to be enabled out of upper, lower, number, special')
    charList = []
    if upper:
        charList += string.ascii_uppercase
    if lower:
        charList += string.ascii_lowercase
    if number:
        charList += string.digits
    if special:
        charList += string.punctuation
    return ''.join(random.SystemRandom().choice(charList) for _ in range(length))