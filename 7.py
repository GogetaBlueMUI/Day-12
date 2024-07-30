def exponent(num, rang):
    for i in range(rang):
        print(f"Result of {num} to power {i} = {num**i}")
num=int(input("Enter a number: "))
rang=int(input("Enter range for exponents: "))
exponent(num,rang)