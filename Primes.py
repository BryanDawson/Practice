"""
Simple prime number practice program.


Solution for:
http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

"""


def is_int(str_val):
    """Returns True if input string contains a 'python safe' integer."""

    try:
        _ = int(str_val)
    except ValueError:
        return False
    return True


def isprime(n):
    """Returns True if n is prime.

    Code borrowed from:
    https://stackoverflow.com/a/1801446
    Nice clean implementation, why reinvent the wheel
    Tested: acceptable interactive performance up to about 16 decimal digits
            ...on a fairly slow virtual machine

    Note: pylint doesn't like these short variable names,
          ... but for this simple module I think they are fine.
    """

    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def main():
    """ Run the check prime program. """

    while True:

        test = input(
            """Choose a number to see if it is prime,
               or type 'exit' to quit: """)

        if test == "exit":  # User exits program
            print("Goodbye! \n\n")
            break

        # Now we do some basic input error validation
        if not is_int(test):
            print(test, "doesn't look like a number, try again")
            continue

        if isprime(int(test)):
            print(test, "is prime!")
        else:
            print(test, "is not prime.")


main()
