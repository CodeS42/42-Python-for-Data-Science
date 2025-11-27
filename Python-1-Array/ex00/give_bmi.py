MIN_HEIGHT = 0.4
MAX_HEIGHT = 2.75
MIN_WEIGHT = 1
MAX_WEIGHT = 450
MIN_BMI = 5
MAX_BMI = 200

HEIGHT = 0
WEIGHT = 1
BMI = 2

import numpy

def is_valid_list(lst, data) -> bool:
    if not lst:
        print("Error: Lists cannot be empty.")
        return False
    if not isinstance(lst, list):
        print("Error: Heights, weights and BMI must be in lists.")
        return False
    for elem in lst:
        if not isinstance(elem, (int, float)):
            print("Error: Lists must contain only integers or floats numbers.")
            return False     
        if data == HEIGHT and (elem < MIN_HEIGHT or elem > MAX_HEIGHT):
            print("Error: Height is out of range.")
            return False
        if data == WEIGHT and (elem < MIN_WEIGHT or elem > MAX_WEIGHT):
            print("Error: Weight is out of range.")
            return False
    return True

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if not (is_valid_list(height, HEIGHT) and is_valid_list(weight, WEIGHT)):
        return None
    if not (len(weight) == len(height)):
        print("Error: The height and weight lists must be the same length.")
        return None

    heights = numpy.array(height)
    weights = numpy.array(weight)
    bmi = weights / (heights**2)
    if numpy.any(bmi < MIN_BMI) or numpy.any(bmi > MAX_BMI):
        print("Error: BMI is not realistic.")
        return None
    
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not is_valid_list(bmi, BMI):
        return None
    if not isinstance(limit, int):
        print("Error: The limit must be an integer.")
        return None
    if limit < MIN_BMI or limit > MAX_BMI:
        print("Error: The limit is out of range.")
        return None

    bool_array = numpy.array(bmi)

    return (bool_array > limit).tolist()


def main():
    # Tests subject
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
    print()

    # Lists of different lengths
    height = [2]
    weight = [55, 25]
    give_bmi(height, weight)
    print()

    # Not a list
    height = "2"
    weight = [55, 25]
    give_bmi(height, weight)
    print()

    # Lists contain an unauthorized type
    height = ['s', 1.5]
    weight = [55, "test"]
    give_bmi(height, weight)
    print()

    # Lists contain values out of range
    height = [999, 1.5]
    weight = [55, 0]
    give_bmi(height, weight)
    print()

    # Empty lists
    height = []
    weight = []
    give_bmi(height, weight)
    print()

    # Limit is not an integer
    bmi = [20, 30.4]
    apply_limit(bmi, "26")
    print()

    # BMI is not realistic
    height = [2.75]
    weight = [1]
    give_bmi(height, weight)
    print()

    # Limit is out of range
    bmi = [18.5]
    apply_limit(bmi, 2)

if __name__ == "__main__":
    main()
