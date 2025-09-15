class NegativeNumberError(Exception):
    """Raised when a negative number is encountered."""
    pass

def check_positive(n: float):
    if n < 0:
        raise NegativeNumberError(f"Number is negative: {n}")
    return n

try:
    check_positive(-3)
except NegativeNumberError as e:
    print("Caught:", e)