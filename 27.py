""""
Realice un menú donde el usuario deberá seleccionar una opción de las
operaciones básicas, y se le solicite al usuario digitar dos números, y
dependiendo de la respuesta realice cada operación.
"""
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
print(f"Basic Operations Menu:")
print(f"1. Addition")
print(f"2. Subtraction")
print(f"3. Multiplication")
print(f"4. Division")
option = int(input("Select an option (1-4): "))
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
if option == 1:
    result = addition(number1, number2)
elif option == 2:
    result = subtraction(number1, number2)
elif option == 3:
    result = multiplication(number1, number2)
elif option == 4:
    result = division(number1, number2)
else:
    print(f"Invalid option. Please select a valid option from the menu.")
    result = None
if result is not None:
    print(f"The result is: {result:.2f}")
