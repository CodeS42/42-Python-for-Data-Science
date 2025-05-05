import sys
from ft_filter import ft_filter

def valid_arguments(args):
    try:
        int(sys.argv[2])
        str(sys.argv[1])
    except ValueError:
        return False
    return True

def main():
    try:
        if not len(sys.argv) == 3 or not valid_arguments(sys.argv[1:]):
            raise AssertionError("AssertionError: the arguments are bad")
        N = int(sys.argv[2])
        S = str(sys.argv[1]).split()
        filterstring = lambda word: len(word) > N
        print(ft_filter(filterstring, S))
    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    main()