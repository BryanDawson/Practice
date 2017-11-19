"""Input handlers for common command line situations"""


def inputintgen(prompt="Enter a number", quitval="exit", posonly=True):
    """ Reads and validates 'number' inputs

        Assumes that 'number' implies an integer, typically positive,
        but non-postive (zero or less) values are also optionally supported

        Does not do extensive type checking -- anything that
        int() conversion can handle without ValueException is considered
        to be a 'number'.

        Implemented as a generator and will continue to return integers
        until 'quitval' string is typed

        Call with quitval set to None is used for no 'quit' prompt
    """

    while True:
        if quitval is None:
            rval = input("{}".format(prompt))
        else:
            rval = input("{},\nor type {} to quit: ".format(prompt, quitval))

        if rval == quitval:  # User stops supplying numbers
            raise StopIteration

        # Now we do some basic input error validation

        try:
            ival = int(rval)
        except ValueError:
            print("{} doesn't look like a number, try again".format(rval))
            continue

        if posonly is True and ival <= 0:
            print("Only positive non-zero values allowed, try again")
            continue

        yield ival


def menuchoice(prompt, options, keyvals):
    """ Returns a validated 'letter' choice from supplied menu

        prompt: prints at the bottom of the options list, wait for user input
        options: list of strings (will print one per line) for user options
        keyvals: list of strings for valid user choices

        NOTE:  I had this working, but then decided to do it differently
                in my main program.  Leaving here in case I need it someday...
    """

    while True:
        for optline in options:
            print(optline)
        choice = input(prompt)

        if choice not in keyvals:
            print("{} is not an option\nPlease try again\n")
            continue
        else:
            return choice
