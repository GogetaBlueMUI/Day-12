def check(number1, number2):
    if((type(number1) in [float, int]) and (type(number2) in [float, int])):
        return number1+number2
    else:
        print("Both the inputs should be a number!")
number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
print("Sum: ", check(number1, number2))