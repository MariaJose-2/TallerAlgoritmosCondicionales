"""Mostrar la suma de dos números enteros, si el resultado supera a 10."""

number1 = int(input("Enter the first number integer: "))
number2 = int(input("Enter the second number integer: "))

sum = number1 + number2

if sum > 10:
    print(f"the sum of {number1} and {number2} is {sum}")
