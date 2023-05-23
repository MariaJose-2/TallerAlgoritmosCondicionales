"""Un trabajador necesita calcular su salario semanal, el cual se obtiene de la
siguiente manera: si trabaja 20 horas o menos se le paga $10.000 por hora; si
trabaja más de 20 horas se le paga $35.000 por hora."""

hours_worked = float(input("Enter the number of hours worked: "))

if hours_worked <= 20:
    weekly_salary = hours_worked * 10000
else:
    weekly_salary = hours_worked * 35000

print(f"The worker's weekly salary is: {weekly_salary}")