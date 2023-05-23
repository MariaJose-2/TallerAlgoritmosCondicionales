"""Algoritmo para hallar el área de un cuadrado si el valor del lado es mayor a
10, de lo contrario generar un mensaje de “no aplica”."""

side = float(input("Enter the value of the square's side: "))
if side > 10:
    area = side ** 2
    print(f"The area of the square is: {area}")
else:
    print(f"Not applicable")
