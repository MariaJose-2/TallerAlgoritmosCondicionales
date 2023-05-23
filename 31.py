"""Realizar el siguiente algoritmo: calcular el salario de un empleado dado el numero de horas, el valor de la hora y la categoria del empleado.
A:10%
B:15%
C:23%
D:25%
"""
numberHours = int(input("Enter the number of hours worked: "))
hourValue = float(input("Enter the value of the hour worked: "))
category = input("Enter the employee's category (A, B, C or D): ")
if category == "A":
    increment = 0.10
if category == "B":
    increment = 0.15
if category == "C":
    increment = 0.23
elif category == "D":
    increment = 0.25
else:
    print(f"Invalid category. Must be A, B, C or D.")
    exit()
salary = numberHours * hourValue
salaryIncreasedSalary = salary + (salary * increment)
print(f"The employee's salary is: {salaryIncreasedSalary}")
