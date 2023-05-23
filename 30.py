""""
Realizar el siguiente algoritmo:
entrada:un numero, que se almacenara en una variable llamada numeroDia. 
proceso:realizar las respectivas comparaciones para cada uno de los valores entre 1 y 7.
salida: mostrar el nombre del dia, segun el valor contenido en numeroDia.
"""
day_number = int(input("Type a number from 1 to 7: "))
if day_number == 1:
    print(f"Monday")
elif day_number == 2:
    print(f"Tuesday")
elif day_number == 3:
    print(f"Wednesday")
elif day_number == 4:
    print(f"Thursday")
elif day_number == 5:
    print(f"Friday")
elif day_number == 6:
    print(f"Saturday")
elif day_number == 7:
    print(f"Sunday")
else:
    print(f"Invalid number. You must enter a value from 1 to 7.")
