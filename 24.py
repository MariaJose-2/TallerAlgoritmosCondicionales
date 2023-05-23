"""Elaborar un programa que compruebe si un año es bisiesto.
Nota: si un año es divisible entre 100, pero no entre 400, entonces "no" es un
año bisiesto. Si un año es divisible entre 100 y 400, entonces "si" es un año
bisiesto. Por ejemplo, 1900 es exactamente divisible entre 100, pero no entre 400, ya
que se obtiene un resultado de 4,75. Esto significa que 1900 no es un año
bisiesto.Por otro lado, 2000 es exactamente divisible entre 100 y 400, ya que da como
resultado 5. Eso significa que el año 2000 es un año bisiesto."""

year = int(input("Enter a year: "))
is_leap = False  
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
    else:
        is_leap = True

if is_leap:
    print(f"is a leap year.{year}")
else:
    print(f"is not a leap year.{year}")

