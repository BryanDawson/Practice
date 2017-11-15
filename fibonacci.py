"""
Simple Fibonacci practice program.


Solution for:
http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
"""


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

    while True:

        length = input(
            """Choose a number for the length of the fibonacci sequence,
               or type 'exit' to quit: """)

        if length == "exit":  # User exits program
            print("Goodbye! \n\n")
            break

        # Now we do some basic input error validation
        if not is_int(length):
            print(length, "doesn't look like a number, try again")
            continue
        elif int(length) < 1:
            print("Zero or negative counts are not allowed, try again")
            continue

        # Build the list of Fibonacci numbers by calling the iterator
        outseq = [val for val in fibit(int(length))]

        # A little loop here to clean up the output when the list is long
        items_per_line = 5
        start = 0
        end = items_per_line
        print(outseq[start:end])
        while end < len(outseq):
            start = end
            end += items_per_line
            print(outseq[start:end])


main()
