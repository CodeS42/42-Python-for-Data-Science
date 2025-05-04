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
        elif len(sys.argv) < 2:
            string = "Hello World!"
            print("What is the text to count?")
            print(string)
        else:
            string = sys.argv[1]

        uppercase_char = sum(character.isupper() for character in string)
        lowercase_char = sum(character.islower() for character in string)
        punctuation_char = sum(ispunctuation(character) for character in string) + 1
        digits = sum(character.isdigit() for character in string)
        spaces = sum(character.isspace() for character in string)
        if len(sys.argv) < 2:
            punctuation_char -= 1
            spaces += 1

        total = uppercase_char + lowercase_char + punctuation_char + digits + spaces

        print(f"The text contains {str(total)} characters:")
        print(f"{str(uppercase_char)} upper letters")
        print(f"{str(lowercase_char)} lower letters")
        print(f"{str(punctuation_char)} punctuation marks")
        print(f"{str(spaces)} spaces")
        print(f"{str(digits)} digits")
        
    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    main()
