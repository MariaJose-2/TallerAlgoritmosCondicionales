"""Hacer un programa que pida 3 números e indicar si el tercero es igual a la
suma del primero y el segundo."""

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

if number3 == number1 + number2:
    print(f"The third number is equal to the sum of the first and second numbers.")
else:
    print(f"The third number is not equal to the sum of the first and second numbers.")