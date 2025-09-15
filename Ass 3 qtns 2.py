def calculate_average(*args):
    """
    Return the arithmetic mean of the provided numeric arguments.

    Parameters:
        *args: One or more int/float values.

    Returns:
        float: The average.

    Raises:
        ValueError: If no numbers are provided.
        TypeError: If any argument is non-numeric.
    """
    if not args:
        raise ValueError("At least one number is required.")
    if not all(isinstance(x, (int, float)) for x in args):
        raise TypeError("All arguments must be numbers.")
    return sum(args) / len(args)