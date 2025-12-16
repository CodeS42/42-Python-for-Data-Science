from typing import Any


def mean(args):
    """Calculate the average (mean) of a list of numbers."""
    return sum(args) / len(args)


def median(args):
    """Return the median value of a list of numbers."""
    sorted_args = sorted(args)
    nb_args = len(sorted_args)
    if nb_args % 2 == 0:
        i = (nb_args // 2) - 1
        j = nb_args // 2
        return (sorted_args[i] + sorted_args[j]) / 2
    else:
        i = nb_args // 2
        return sorted_args[i]


def quartile(args):
    """Compute the first and third quartiles of a list."""
    sorted_args = sorted(args)
    len_args = len(sorted_args)
    q1_i = len_args // 4
    q3_i = len_args * 3 // 4
    if len_args % 4 == 0:
        q1 = (sorted_args[q1_i - 1] + sorted_args[q1_i]) / 2
        q3 = (sorted_args[q3_i - 1] + sorted_args[q3_i]) / 2
    else:
        q1 = sorted_args[q1_i]
        q3 = sorted_args[q3_i]
    return [float(q1), float(q3)]


def var(args):
    """Calculate the variance of a list of numbers."""
    mean_args = mean(args)
    gap =\
        [nb - mean_args if nb >= mean_args else mean_args - nb for nb in args]
    gap_positive = [nb**2 for nb in gap]
    return mean(gap_positive)


def std(args):
    """Calculate the standard deviation of a list of numbers."""
    return var(args) ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Perform statistical calculations based on the requested kwargs.
    Supported kwargs: 'mean', 'median', 'quartile', 'var', 'std'."""
    try:
        types = kwargs.values()
        for t in types:
            if not args:
                print("ERROR")
            else:
                if t == "mean":
                    print(f"mean : {mean(args)}")
                elif t == "median":
                    print(f"median : {median(args)}")
                elif t == "quartile":
                    print(f"quartile : {quartile(args)}")
                elif t == "var":
                    print(f"var : {var(args)}")
                elif t == "std":
                    print(f"std : {std(args)}")
    except Exception as e:
        print(f"Error: {e}")
