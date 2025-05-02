import sys

try:
    if len(sys.argv) > 2:
        raise AssertionError("AssertionError: more than one argument is provided")
    
    if  % 2 == 0:
        print("I'm Even.")
    else :
        print("I'm Odd.")
except AssertionError as e:
    print(e)

try:
    number = int(sys.argv[1])
except Exception:
    
