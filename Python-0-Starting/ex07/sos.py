import sys


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    "0": "----- "
}


def wrong_character(S):
    if not S:
        return True
    for c in S:
        if not c.isalpha() and not c.isdigit() and not c.isspace():
            return True
    False


def convert_string(S):
    new_string = ""
    S = S.upper()

    for c in S:
        new_string += NESTED_MORSE[c]
    new_string = new_string[:-1]

    return new_string


def main():
    try:
        if len(sys.argv) != 2 or wrong_character(sys.argv[1]):
            raise AssertionError("AssertionError: the arguments are bad")

        print(convert_string(sys.argv[1]))
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
