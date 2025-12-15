from typing import Any

def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal limit, function, count
            if count < limit:
                function()
            else:
                print(f"Error: {function} call too many times")
            count += 1
        return limit_function
    return callLimiter