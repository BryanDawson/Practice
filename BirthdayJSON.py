"""
Simple practice program stores birthdays in a JSON

Solution for:
http://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html
http://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html
http://www.practicepython.org/exercise/2017/02/28/35-birthday-months.html
http://www.practicepython.org/exercise/2017/04/02/36-birthday-plots.html

"""

import json
import calendar
from collections import Counter
from pprint import pprint as pp
from bokeh.plotting import figure, show, output_file
from InputHandler import menuchoice


def to_json(filename, collection):
    """Writes the collection as a JSON into file"""
    with open(filename, "w") as outfile:
        json.dump(collection, outfile, indent=4)


def from_json(filename):
    """Returns a collection with the JSON data from file

       Raises errors for file not found or invalid JSON"""
    try:
        with open(filename, "r") as infile:
            return json.load(infile)
    except FileNotFoundError:
        raise FileNotFoundError
    except ValueError:   # JSONDecodeError is a subclass of ValueError
        raise ValueError


def initialize(filename):
    """ Ensure that the JSON file exists and is readable, create one if necessary

        Side Effect: Creates a JSON file if none exists by the specified name
        Returns the JSON as supplied by json.load()
    """

    test_data = {
        "Leonardo Da Vinci": "April 15, 1452",
        "Isaac Newton": "January 4, 1643",
        "Albert Einstein": "March 14, 1879",
        "Galileo Galilei": "February 15, 1564",
        "Nikola Tesla": "July 10, 1856",
        "Wolfgang Amadeus Mozart": "January 27, 1756",
        "George Washington": "February 22, 1732",
        "Thomas Jefferson": "April 13, 1743",
        "Abraham Lincoln": "February 12, 1809",
        "Benjamin Franklin": "January 17, 1706"
    }

    try:
        return from_json(filename)
    except FileNotFoundError:  # If file not found, create one
        to_json(filename, test_data)
        return from_json(filename)
    except ValueError:  # Die gracefully if not valid JSON
        print("Input file doesn't contain valid JSON")
        exit(ValueError)


def find_action(bdays):
    """Perform the user requested 'Find' action"""

    findname = input("\nType a name to find the birthday\n"
                     " Examples: try 'George Washington'\n"
                     "            or   'Albert Einstein': ")
    try:
        foundbday = bdays[findname]
    except KeyError:
        print("\nNo names found matching: ", findname, "\n")
        return

    print("\n Found", findname + ", who's birthday is: ", foundbday, "\n")


def add_action(filename, bdays):
    """Perform the user requested 'Add' action

    No attempt to validate input
    """

    addname = input("\nType the full name of the person to be added: ")
    addbday = input("Now type the corresponding birthday: ")

    bdays[addname] = addbday
    to_json(filename, bdays)

    print("\n", addname, "Has been added with birthday: ",
          addbday, "\n")


def extract_months(bdays):
    """Returns a list of the month names from the dict values"""

    return [bday.split()[0] for bday in list(bdays.values())]


def count_action(bdays):
    """Perform the user requested 'Count' action

       Note: The 'specification' is conflicting.  It shows the desired
                output looking "like a dict" but also looking sorted.
                since there is no easy way to achieve BOTH, this just
                does "like a dict", but unsorted.  Plot_action() uses
                a sorted version.
    """

    # Now we can produce the requested count of months
    print("\nHere is the count of birthdays by month:\n\n")
    pp(dict(Counter(extract_months(bdays))))
    print("\n")


def plot_action(bdays):
    """Peform the user requested 'Plot' action"""

    bday_months = extract_months(bdays)
    bday_count = Counter(bday_months)

    # Produce a list of all 12 months in month order
    xvals = list(calendar.month_name)[1:]
    # Extract a list of the counts for all months in month order
    yvals = [bday_count[month_name] for month_name in xvals]

    output_file("BdayPlot.html")
    x_categories = list(calendar.month_name)[1:]

    bok_pl = figure(plot_width=1000,
                    x_range=x_categories)
    bok_pl.vbar(x=xvals, top=yvals, width=0.5)

    show(bok_pl)


def main():
    """Run the main Birthday program"""

    bdays_filename = "birthdays.json"
    actionmenu = [
        "F Find a birthday by name",
        "A Add a name and birthday",
        "C Show count of birthdays by month",
        "P Plot the birthdays by month",
        "X Exit the program"
        ]
    actionkeys = ['F', 'f', 'A', 'a', 'C', 'c', 'X', 'x', 'P', 'p']
    actionprompt = "Please choose an option: "

    # Load or create the JSON as appropriate
    bdays = initialize(bdays_filename)

    while True:
        action = menuchoice(actionprompt, actionmenu, actionkeys)
        action = action.upper()
        if action == 'F':
            find_action(bdays)
        elif action == 'A':
            add_action(bdays_filename, bdays)
        elif action == 'C':
            count_action(bdays)
        elif action == 'P':
            plot_action(bdays)
        elif action == 'X':
            print("Goodbye!\n")
            break


main()
