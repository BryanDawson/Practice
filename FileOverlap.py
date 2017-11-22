"""
Simple find common integers between two files practice program

Solution for:
http://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html

Assumptions:
    1. Each file contains an increasing order list
       of valid integers, one per line.
    2. Both files will comfortably fit in memory
       (as a later exercise, eliminate this assumption)
"""


def main():
    """Run the file overlap program"""
    with open('primenumbers.txt') as pfile:
        ptxt = pfile.read()

    with open('happynumbers.txt') as hfile:
        htxt = hfile.read()

    # Convert both lists of newline separated strings to lists of ints
    plst = list(map(int, ptxt.split("\n")))
    hlst = list(map(int, htxt.split("\n")))

    olst = [num for num in plst if num in hlst]

    print("The common numbers between these two files are:\n", olst)


main()
