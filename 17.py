"""Hacer un programa que pida dos números y los imprima en forma
ascendente y descendente."""

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print("Ascending order:")
if number1 < number2:
    print(number1, number2)
else:
    print(number2, number1)

print("Descending order:")
if number1 > number2:
    print(number1, number2)
else:
    print(number2, number1)
