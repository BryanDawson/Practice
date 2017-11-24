"""
Simple practice program stores birthdays in a JSON

Solution for:
http://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html


"""

import json
from InputHandler import menuchoice

VERBOSE = False


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
    except ValueError:
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
    except FileNotFoundError:  # If file not found, we make one
        to_json(filename, test_data)
        return from_json(filename)
    except ValueError:  # Die gracefully if not valid JSON
        print("Input file doesn't contain valid JSON")
        exit(ValueError)


def find_action(bdays):
    """Perform the user requested 'Find' action"""

    findname = input("\nType a name to find the birthday\n"
                     " (examples: try 'George Washington'\n"
                     "            or   'Albert Einstein': ")
    try:
        foundbday = bdays[findname]
    except KeyError:
        foundbday = ""
    if foundbday:
        print("\n Found", findname + ", who's birthday is: ",
              foundbday, "\n")
    else:
        print("\nNo names found matching: ", findname, "\n")


def main():
    """Run the main Birthday program"""

    actionmenu = [
        "F Find a birthday by name",
        "A Add a name and birthday",
        "C Show count of birthdays by month",
        "X Exit the program"
        ]
    actionkeys = ['F', 'f', 'A', 'a', 'C', 'c', 'X', 'x']
    actionprompt = "Please choose an option: "

    # Load or create the JSON as appropriate
    bdays = initialize("birthdays.json")

    while True:
        action = menuchoice(actionprompt, actionmenu, actionkeys)
        action = action.upper()
        if VERBOSE:
            print(action)
        if action == 'F':
            find_action(bdays)
        elif action == 'A':
            print('\n', action, "is not yet implemented\n")
        elif action == 'C':
            print('\n', action, "is not yet implemented\n")
        elif action == 'X':
            print("Goodbye!\n")
            break


main()
