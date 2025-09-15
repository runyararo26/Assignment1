def divide_numbers(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: division by zero.")
    except TypeError:
        print("Error: inputs must be numbers.")

print(divide_numbers(10, 2))    # 5.0
print(divide_numbers(10, 0))    # prints error
print(divide_numbers("10", 2))  # prints error