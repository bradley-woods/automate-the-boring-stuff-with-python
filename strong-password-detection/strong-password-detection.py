# Automate the Boring Stuff with Python
# Chapter 7 - Pattern Matching with Regular Expressions: Strong Password Detection

import re

def checkPassword(password):
    # Match password of min. 8 characters, min. 1 uppercase and min. 1 digit
    strongPassword = re.match(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}', password)
    return bool(strongPassword)


print("Strong password: " + str(checkPassword("abcABC123")))
