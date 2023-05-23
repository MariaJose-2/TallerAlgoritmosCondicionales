"""A un trabajador le descuentan de su sueldo el 4%, si su sueldo es menor o
igual a $1.000.000, si el sueldo está entre $1.000.000 y $2.000.000 el 7%, y por
encima de 2.000.000 el 8% calcular el descuento y sueldo neto que recibe el
trabajador dado su sueldo."""
salary=float(input("what is your salary?"))
if salary<=1000000:
    discount=0.04
    net_salary=salary-discount
elif salary>=1000000 and salary<=2000000:
    discount=0.07
    net_salary=salary-discount
elif salary>2000000:
    discount=0.08
    net_salary=salary-discount
print(f"his net salary is:: {net_salary}")
print(f"the discount was: {discount} %")
