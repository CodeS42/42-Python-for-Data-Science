from typing import Any


def callLimit(limit: int):
    """Decorator factory that limits the number of times a function
    can be called."""
    count = 0

    def callLimiter(function):
        """Decorator that wraps a function to enforce a call limit."""

        def limit_function(*args: Any, **kwds: Any):
            """Wrapper function that counts calls and blocks execution
            when the call limit is exceeded."""
            nonlocal count
            if count < limit:
                function(*args, **kwds)
                count += 1
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
