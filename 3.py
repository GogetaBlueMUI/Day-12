def round_float(value, strategy):
    if strategy == "up":
        return int(value) + (value > int(value)) #the truth value is 1 so it adds 1 to the int value
    elif strategy == "down":
        return int(value)
    elif strategy == "nearest":
        return round(value)
    else:
        raise ValueError("Invalid rounding strategy. Choose 'up', 'down', or 'nearest'.")
value=float(input("Enter number: "))
strategy=input("Enter up, down or nearest: ")
print("Output: ", round_float(value, strategy))
