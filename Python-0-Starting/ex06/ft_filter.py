def ft_filter(func, iterable_value):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    return [element for element in iterable_value if func(element)]
