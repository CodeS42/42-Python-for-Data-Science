import sys

def ispunctuation(character):
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    for sign in punctuation:
        if character == sign:
            return True
    
    return False

def main():
    try :
        if len(sys.argv) > 2:
            raise AssertionError("AssertionError: more than one argument is provided")
        # elif len(sys.argv) < 2: 
        string = sys.argv[1]
        uppercase_char = sum(character.isupper() for character in string)
        lowercase_char = sum(character.islower() for character in string)
        punctuation_char = sum(ispunctuation(character) for character in string)
        digits = sum(character.isdigit() for character in string)
        spaces = sum(character.isspace() for character in string)
        
    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    main()
