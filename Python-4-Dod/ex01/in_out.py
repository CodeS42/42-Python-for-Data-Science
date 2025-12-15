def square(x: int | float) -> int | float:
    """Returns the square of a number."""
    try:
        return x**2
    except Exception as e:
        print(f"Error: {e}")
        return None


def pow(x: int | float) -> int | float:
    """Returns the exponentiation of a number by itself."""
    try:
        return x**x
    except Exception as e:
        print(f"Error: {e}")
        return None


def outer(x: int | float, function) -> object:
    """Returns a function that applies a given operation to a stored value.
    The returned function keeps an internal state and updates the value each
    time it is called by applying the provided function."""
    count = 0

    def inner() -> float:
        """Updates the stored value using the provided function.
        Each call applies the function to the current value, updates it, and
        returns the new value."""
        nonlocal x, count
        x = function(x)
        count += 1
        return x
    return inner
