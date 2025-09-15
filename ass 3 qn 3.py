while True:
    s = input("Enter a number: ")
    try:
        x = float(s)
        print("You entered:", x)
        break
    except ValueError:
        print("Not a valid number. Try again.")