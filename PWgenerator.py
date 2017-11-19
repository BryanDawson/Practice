"""
Simple Password Generator practice program.


Solution for:
http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
"""

from random import choice, choices, shuffle
import string
from InputHandler import inputintgen

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%"  # Password systems are inconsistent, so use only these 'safe' symbols


def pwgen(pwlength, pwtypes):
    """ Returns generated password as a string

        pwlength: integer length of the password
        pwtypes: List of strings chosen from LOWER, UPPER, DIGITS, and SYMBOLS
    """

    outstring = ""

    # First make sure that at least one of each type is in the string
    # later the string will be shuffled to eliminate any implied type order

    for pwtype in pwtypes:
        outstring += choice(pwtype)

    # Add another random string to get the required length
    if len(outstring) < pwlength:
        outstring += ''.join(choices(''.join(pwtypes),
                                     k=(pwlength - len(outstring))))

    # Shuffle the password string to eliminate any implied type order
    lchars = list(outstring)
    shuffle(lchars)
    outstring = ''.join(lchars)

    return outstring


def main():
    """ Run the password generator program"""

    # Walk the user through some choices
    passlen = next(inputintgen(
        "Note: provided passwords will always be at least 4 characters \n"
        "  Choose a length for your passwords: ", None))
    if passlen < 4:
        passlen = 4

    typechoice = input(
        "OPTIONS:\n"
        "L Password must contain lowercase Letters\n"
        "U Password must contain uppercase Letters\n"
        "D Password must contain numeric digits\n"
        "S Password must contain Symbols\n"
        "Type some letters describing your choice: \n"
        "  Examples: you could type LD, UDS, or LUDS  "
    )

    # Notes:
    #           Silently ignore any garbage in the input
    #           Permit options in upper or lower case
    #           Defaults to L (lowercase) if no valid options found

    typechoice = typechoice.upper()

    # Comprehension using a local dict to decode the letters
    passtypes = [
        {
            'L': LOWER,
            'U': UPPER,
            'D': DIGITS,
            'S': SYMBOLS}[letter]
        for letter in typechoice if letter in "LUDS"
    ]

    if not passtypes:
        passtypes.append(LOWER)

    # Now generate and print passwords based on the user specifications
    print("Each time you press ENTER, a new password will be generated,\n",
          "Type anything else to terminate.")
    while input() == "":
        print(pwgen(passlen, passtypes))


main()
