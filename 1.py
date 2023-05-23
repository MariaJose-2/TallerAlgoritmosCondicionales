"""""
Diseñe un algoritmo que capture dos números, y que realice la suma de
dichos números, y mostrar los datos si es el resultado no es negativo.
"""
number1 = float(input("enter the first number: "))
number2 = float(input("enter the second number: "))
sum = number1 + number2
if sum >= 0:
    print(f"the result of the sum is:{sum}")
else:
    print(f"the result of the sum is negative.")
