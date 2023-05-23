"""""
Diseñar un algoritmo que muestre si una persona tiene ingresos o no, debe
indicarlos ingresos y egresos, se debe validar el saldo , pero para ser más
específicos se responderá a las siguientes preguntas:
Si no tiene efectivo entonces está en números rojos.
Si tiene poco efectivo menor a 2000, que muestre que debe esforzarse por
trabajar más.
Si tiene un efectivo menor a 3000 entonces significa que le va regularmente
bien.
Si tiene un efectivo mayor a 3000 entonces significa que tiene buen status
financiero.
"""
income = float(input("Enter your income: "))
expenses = float(input("Enter your expenses: "))
balance = income - expenses
if balance == 0:
    print(f"He doesn't have cash. It's in the red.")
elif balance < 2000:
    print(f"You should try to work more.")
elif balance < 3000:
    print(f"he does regularly well.")
else:
    print(f"He has good financial status.")