"""Input handlers for common command line situations"""


def inputintgen(prompt="Enter a number", quitval="exit", negallowed=False):
    """ Reads and validates 'number' inputs

        Assumes that 'number' implies an integer, typically positive,
        but negative values are also optionally supported

        Does not do extensive type checking -- anything that
        int() conversion can handle without ValueException is considered
        to be a 'number'.

        Implemented as a generator and will continue to return integers
        until 'quitval' string is typed
    """

    while True:
        rval = input("{},\nor type {} to quit: ".format(prompt, quitval))

        if rval == quitval:  # User stops supplying numbers
            raise StopIteration

        # Now we do some basic input error validation

        try:
            ival = int(rval)
        except ValueError:
            print("{} doesn't look like a number, try again".format(rval))
            continue

        if negallowed is False and ival < 0:
            print("Negative numbers are not allowed, try again")
            continue

        yield ival
