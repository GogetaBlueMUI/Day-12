def divide_and_round(num1, num2, precision):
    if num2 == 0:
        print("Division by zero is not allowed.")
    result = num1 / num2
    result = round(result, precision)
    print("Output: ", result)
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
precision=int(input("Enter precision: "))
divide_and_round(num1, num2, precision)