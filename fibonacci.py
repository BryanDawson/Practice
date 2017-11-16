"""
Simple Fibonacci practice program.


Solution for:
http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
"""
from pprint import pprint as pp

from InputHandler import inputintgen



def is_int(str_val):
    """Returns True if input string contains a 'python safe' integer."""

    try:
        _ = int(str_val)
    except ValueError:
        return False
    return True


""" recursive version is elegant but very inefficient for large count
def fib(count):
    ""Returns the Nth Fibonacci calculated recursively""

    if count <=2:
        return 1
    else:
        return fib(count-1) + fib(count-2)
"""


def fibit(count):
    """Yeilds (as an generator) Fibonacci numbers up to count

       Assumes that count is non-zero and positive
    """

    prev = [1, 0]
    i = 0
    while i < count:
        nxt = sum(prev)
        prev[0] = prev[1]
        prev[1] = nxt
        yield nxt
        i += 1


def main():
    """ Run the fibonacci program. """

    for length in inputintgen("Choose a number for the length of the fibonacci sequence"):

        # Build the list of Fibonacci numbers by calling the iterator
        outseq = [val for val in fibit(int(length))]

        # Use pprint to make the output nice for long lists
        pp(outseq, compact=True)

    # User stopped providing numbers
    print("Goodbye!\n")


main()
