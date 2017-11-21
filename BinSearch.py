"""
Simple binary search practice program.

Added some timings and a comparison with python builtin index()
for very large lists, the binary search is dramatically faster,
   ...as expected


Solution for:
http://www.practicepython.org/exercise/2014/11/11/20-element-search.html
"""

from random import sample, choice, randrange
from timeit import default_timer as dtime


def pysearch(item, seq):
    """ Returns index of item in sequence, or None if not found

    We will use this to test timing of different search algorithms
    This version uses python builtin index function

    :param item: integer to be found in the sequence
    :param seq: ascending list of integers to search
    :return: index of found item, or None if item not found
    """

    try:
        return seq.index(item)
    except ValueError:
        return None


def binsearch(item, seq):
    """ Returns index of item in sequence, or None if not found

    We will use this to test timing of different search algorithms
    This version uses hand coded binary search

    :param item: integer to be found in the sequence
    :param seq: ascending list of integers to search
    :return: index of found item, or None if item not found
    """

    upper = len(seq) - 1
    lower = 0
    mid = upper // 2

    while seq[mid] != item and upper > lower + 1:
        if seq[mid] > item:
            upper = mid
            mid = lower + ((upper - lower) // 2)
        else:
            lower = mid
            mid = lower + ((upper - lower) // 2)

    if seq[mid] == item:
        return mid

    return None


def main():
    """Run the binary search program"""

    verbose = False

    print(
        "Program runs two diferent search algorithms\n"
        "  (python index() and binary search)\n"
        "on lists of increasing size\n\n"
        "Output is the timing ratio between the two algorithms"
    )
    for listnum in range(3, 7):
        # Create a nice sorted list of integers for testing
        listlen = 10**listnum
        testlist = sample(range(10*listlen), listlen)
        testlist.sort()

        # Now set up two values for testing,
        # One that is in the list, and one that is not
        inlist = choice(testlist)
        # Most of the time this loop will break immediately
        while True:
            notinlist = randrange(1000)
            if notinlist not in testlist:
                break

        if verbose:
            print(testlist)
            print(inlist)
            print(notinlist)

        start_time = dtime()
        indx1 = pysearch(inlist, testlist)
        indx2 = pysearch(notinlist, testlist)
        elapsed1 = dtime() - start_time

        if verbose:
            print(indx1)
            print(indx2)
            print(elapsed1)

        start_time = dtime()
        indx1 = binsearch(inlist, testlist)
        indx2 = binsearch(notinlist, testlist)
        elapsed2 = dtime() - start_time

        if verbose:
            print(indx1)
            print(indx2)
            print(elapsed2)

        print("For a list of length", listlen,
              "\nBinary search was faster by a factor of:", elapsed1/elapsed2,
              "\n")


main()
