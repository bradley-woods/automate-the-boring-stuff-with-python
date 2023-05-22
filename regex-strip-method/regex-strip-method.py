# Automate the Boring Stuff with Python
# Chapter 7 - Pattern Matching with Regular Expressions: Regex Version of the strip() Method

import re

def regexStrip(string, remove = " "):
    if remove == "":
        return string
    elif remove == " ":
        # Remove whitespace
        strippedString = re.sub(rf'^{remove}*', "", string)
        strippedString = re.sub(rf'{remove}*$', "", strippedString)
    else:
        # Remove characters entered into second argument
        strippedString = re.sub(rf'^[{remove}]*', "", string)
        strippedString = re.sub(rf'[{remove}]*$', "", strippedString)
    return strippedString


print(regexStrip("   ___---test_string,,,...   ", " .,-_"))
