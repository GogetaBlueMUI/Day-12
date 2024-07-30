def format_integer(number, specifier):
    if specifier.startswith('digits'):
        try:
            length = int(specifier[6:])
            return f"{number:0{length}}"
        except:
            print("Invalid number format in specifier.")
    elif specifier == 'scientific':
        return f"{number:.2e}"
    else:
        print("Unsupported specifier. Use 'digitsN' or 'scientific'.")
number=int(input("Enter number: "))
specifier=input("Enter digits or scientific: ")
print("Output: ", format_integer(number, specifier))