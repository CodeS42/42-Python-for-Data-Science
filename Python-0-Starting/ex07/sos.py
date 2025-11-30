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
    """
    Check if each character in the string is a letter, a number, or a space.

    Args:
        S: the string to analyze.

    Returns:
        True: if the character is forbidden.
        False: if all the characters are allowed.
    """
    for c in S:
        if not c.isalpha() and not c.isdigit() and not c.isspace():
            return True
    return False


def convert_string(S):
    """
    Convert a string to Morse code.

    Args:
        S: the string to convert.

    Returns
        new_string: the string after conversion.
    """
    new_string = ""
    S = S.upper()

    for c in S:
        new_string += NESTED_MORSE[c]
    new_string = new_string[:-1]

    return new_string


def main():
    """
    Main function to handle input validation and convert a string to
    Morse code.

    Behavior:
        - Expects one command-line argument (the string to convert).
        - Raises AssertionError if:
            - The number of arguments is incorrect
            - The string is empty
            - The string contains forbidden characters
        - Prints the Morse code conversion of the input string.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        if not sys.argv[1]:
            raise AssertionError("the string cannot be empty")
        if wrong_character(sys.argv[1]):
            raise AssertionError("the arguments are bad")
        print(convert_string(sys.argv[1]))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
