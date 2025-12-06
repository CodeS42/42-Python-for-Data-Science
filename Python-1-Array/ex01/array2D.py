import numpy as np


def check_2d_array(family):
    """
    Check that the input is a valid 2D list.

    This function verifies that the structure is not empty, that each element
    is a list, and that all sublists have the same length. It also ensures
    that none of the inner lists are empty.

    It raises an exception if any of these conditions are not met.
    """
    if not family:
        raise ValueError("ValueError: Array cannot be empty.")
    first_size = len(family[0])
    for lst in family:
        if not lst:
            raise ValueError("ValueError: Lists cannot be empty.")
        if not isinstance(lst, list):
            raise TypeError("TypeError: Array must contain lists.")
        if not len(lst) == first_size:
            raise ValueError("ValueError: Lists must have the same size.")


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D list between two indices and return the selected rows.

    This function first checks that the provided indices are integers and
    that the input is a valid 2D list. It then extracts the rows between
    the start and end indices and prints the shape of the original and
    sliced arrays.

    If an error occurs during validation or slicing, the function prints
    the exception and returns None.
    """
    try:
        if not (isinstance(start, int) and isinstance(end, int)):
            raise TypeError("TypeError: Start and end must be integers.")
        check_2d_array(family)
        family_array = np.array(family)
        print(f"My shape is : {family_array.shape}")
        new_family_array = np.array(family[start:end])
        print(f"My new shape is : {new_family_array.shape}")
        return family[start:end]
    except Exception as e:
        print(e)
        return None
