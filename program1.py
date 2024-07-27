#
# Calculator Program
#
def addition(num1, num2):
    print(f'Result: {str(num1 + num2)}')

def subtraction(num1, num2):
    print(f'Result: {str(num1 - num2)}')

def multiplication(num1, num2):
    print(f'Result {str(num1 * num2)}')

def division(num1, num2):
    print(f'Result: {num1 / num2}')

while True:
    print("*******************************")
    symbol = input("Enter a symbol: ")

    if symbol in ("+", "-", "*", "/"):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if symbol == "+":
            f'Result: {addition(num1,num2)}'
        elif symbol == "-":
            f'Result: {subtraction(num1, num2)}'
        elif symbol == "*":
            f'Result: {multiplication(num1, num2)}'
        elif symbol == "/":
            try:
                f'Result: {division(num1, num2)}'
            except ZeroDivisionError:
                print("You cannot divide a number by zero.")
        else:
            print("*******************************")