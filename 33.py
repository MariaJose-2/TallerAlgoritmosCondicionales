"""Indicar si entre dos números si ambos son pares o uno de ellos cual es par"""
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
if number1 % 2 == 0 and number2 % 2 == 0:
    print(f"Both numbers are even.")
elif number1 % 2 == 0:
    print(f"The first number is even.")
elif number2 % 2 == 0:
    print(f"The second number is even.")
else:
    print(f"None of the numbers is even.")