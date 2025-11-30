import sys
from ft_filter import ft_filter


def valid_arguments(args):
    """
    Check if the provided arguments are valid: the first argument should be a
    string, the second argument should be an integer.

    Args:
        args: List of command-line arguments.

    Returns:
        True: if the first argument can be cast to string and the second to int
        False: otherwise.
    """
    try:
        int(sys.argv[2])
        str(sys.argv[1])
    except ValueError:
        return False
    return True


def main():
    """
    Main function to filter words in a string that are longer
    than a given length.

    Behavior:
        - Expects two command-line arguments:
            1. A string containing words separated by spaces
            2. An integer N
        - Raises AssertionError if:
            - Number of arguments is not 2
            - Arguments are not of correct types
            - The string contains no words
            - Any word contains non-alphanumeric characters
        - Uses ft_filter to return a list of words whose length
        is greater than N and prints the result.
    """
    try:
        if not len(sys.argv) == 3 or not valid_arguments(sys.argv[1:]):
            raise AssertionError("the arguments are bad")
        N = int(sys.argv[2])
        string = str(sys.argv[1])
        S = string.split()
        if not S:
            raise AssertionError("string does not contain any words")
        for elem in S:
            if not elem.isalnum():
                raise AssertionError("string contains forbidden characters")
        print(ft_filter(lambda word: len(word) > N, S))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
