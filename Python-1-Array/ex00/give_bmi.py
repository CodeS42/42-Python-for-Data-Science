import numpy


MIN_HEIGHT = 0.4
MAX_HEIGHT = 2.75
MIN_WEIGHT = 1
MAX_WEIGHT = 450
MIN_BMI = 5
MAX_BMI = 200
HEIGHT = 0
WEIGHT = 1
BMI = 2


def check_list(lst, data):
    """
    Check that a list of numerical values is valid for
    heights, weights, or BMI.

    This function ensures that the list is not empty, that it contains only
    numbers, and that all values are within realistic ranges depending on the
    type of data.

    It raises an exception if any of these conditions are not met.
    """
    if not lst:
        raise ValueError("ValueError: Lists cannot be empty.")
    if not isinstance(lst, list):
        raise TypeError("TypeError: Heights, weights and BMI must be in \
lists.")
    for elem in lst:
        if not isinstance(elem, (int, float)):
            raise TypeError("TypeError: Lists must contain only integers \
or floats numbers.")
        if data == HEIGHT and (elem < MIN_HEIGHT or elem > MAX_HEIGHT):
            raise ValueError("ValueError: Height is out of range.")
        if data == WEIGHT and (elem < MIN_WEIGHT or elem > MAX_WEIGHT):
            raise ValueError("ValueError: Weight is out of range.")


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """
    Calculate the BMI for a list of heights and weights.

    This function first checks that the input lists are valid and have the
    same length.It then computes the BMI for each pair of height and weight.

    If any BMI value is unrealistic, an exception is raised.
    The result is returned as a list.
    """
    try:
        check_list(height, HEIGHT)
        check_list(weight, WEIGHT)
        if not (len(weight) == len(height)):
            raise ValueError("ValueError: The height and weight lists must \
be the same length.")
        heights = numpy.array(height)
        weights = numpy.array(weight)
        bmi = weights / (heights**2)
        if numpy.any(bmi < MIN_BMI) or numpy.any(bmi > MAX_BMI):
            raise ValueError("ValueError: BMI is not realistic.")
        return bmi.tolist()
    except Exception as e:
        print(e)
        return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Compare each BMI value to a given limit and return a list of boolean
    results.

    This function checks that the BMI list is valid and that the limit
    is an integer within the allowed range. Each BMI value is then
    compared to the limit.

    The result is returned as a list of True or False values.
    """
    try:
        check_list(bmi, BMI)
        if not isinstance(limit, int):
            raise TypeError("TypeError: The limit must be an integer.")
        if limit < MIN_BMI or limit > MAX_BMI:
            raise ValueError("ValueError: The limit is out of range.")
        bool_array = numpy.array(bmi)
        return (bool_array > limit).tolist()
    except Exception as e:
        print(e)
        return None
