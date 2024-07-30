def conversion(input_str, default_value):
    try:
        num = int(input_str)
        return num
    except:
        return default_value
input = input("Enter string: ")
result = conversion(input, 0)
print("Converted Output in Integer:", result)