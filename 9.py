"""
Determinar si un aprendiz aprueba o reprueba una formación, sabiendo que
aprobara si su promedio de tres calificaciones es mayor o igual a 10;
reprueba en caso contrario.
"""
qualification1 = float(input("enter rating 1: "))
qualification2 = float(input("enter rating 2: "))
qualification3 = float(input("enter rating 3: "))

average = (qualification1 + qualification2 + qualification3) / 3

if average >= 10:
    result = "approved"
else:
    result = "reprobate"

print(f"the apprentice this {result} with an average of {average}")