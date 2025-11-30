import sys


def is_punctuation(c):
    """
    Check if the character is a punctuation mark.

    Args:
        c: A single character.

    Returns:
        True: if the character is a punctuation mark.
        False: if the character is not a punctuation mark.
    """
    punc = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    for sign in punc:
        if c == sign:
            return True

    return False


def print_string_details(string):
    """
    Count and print the number of uppercase letters, lowercase letters,
    punctuation marks, digits, and spaces in a string.

    Args:
        string: The text to analyze.
    """
    upp_char = sum(c.isupper() for c in string)
    low_char = sum(c.islower() for c in string)
    punc_char = sum(is_punctuation(c) for c in string)
    digits = sum(c.isdigit() for c in string)
    spaces = sum(c.isspace() for c in string)

    total = upp_char + low_char + punc_char + digits + spaces

    print(f"The text contains {str(total)} characters:")
    print(f"{str(upp_char)} upper letters")
    print(f"{str(low_char)} lower letters")
    print(f"{str(punc_char)} punctuation marks")
    print(f"{str(spaces)} spaces")
    print(f"{str(digits)} digits")


def main():
    """
    Main program function that handles input and calls the analysis function.

    Behavior:
        - If more than one argument is provided, raises AssertionError.
        - If no argument is provided, prompts the user for input and reads
        it from stdin.
        - Otherwise, uses the first command-line argument as the string
        to analyze.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) < 2 or not sys.argv[1]:
            print("What is the text to count?")
            string = sys.stdin.readline()
        else:
            string = sys.argv[1]
        print_string_details(string)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
