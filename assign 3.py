def classify_number(n: int) -> str:
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"

while True:
    try:
        n = int(input("Enter an integer: "))
        print(classify_number(n))
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")
