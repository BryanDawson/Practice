"""
Simple practice program stores birthdays in a JSON

Solution for:
http://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html


"""

import json


def to_json(filename, collection):
    """Writes the collection as a JSON into file"""
    with open(filename, "w") as outfile:
        json.dump(collection, outfile, indent=4)


def from_json(filename):
    """Returns a collection with the JSON data from file
       Note: assumes valid JSON, no error handling"""
    with open(filename, "r") as infile:
        return json.load(infile)


def round_trip_test():
    """ Perform a test that data can round trip via JSON file

        Side Effect: leaves a "birthdays.json" file
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
    to_json("birthdays.json", test_data)
    rtrip = from_json("birthdays.json")
    if test_data == rtrip:
        print("Successful round trip via JSON")


def main():
    """Run the main Birthday program"""

    verbose = True
    if verbose:
        round_trip_test()


main()
