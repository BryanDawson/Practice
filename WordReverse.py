"""
Simple Word reverse practice program.


Solution for:
http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

"""


def revstr(fstr):
    """Returns the  input string in reversed order"""

    tmp = fstr.split()
    print(tmp)
    tmp = tmp[::-1]
    return ' '.join(tmp)


def main():
    """ Run the word reverse program. """

    while True:

        fwdstr = input(
            """Enter any string to reverse,
               or press Enter key to quit: """)

        if fwdstr == "":  # User exits program
            print("Goodbye!\n")
            break

        print(revstr(fwdstr))


main()
