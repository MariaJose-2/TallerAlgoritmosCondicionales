"""En un Almacén de cadena, se hace una promoción mediante la cual el
cliente obtiene un descuento dependiendo de un número que se escoge al
azar, si el número escogido es menor a 65 el descuento es del 20% sobre el
total de la compra si es mayor o igual a 65 el descuento es del 30%."""

import random
chosen_number = random.randint(1, 100)
total_purchase = float(input("Enter the total purchase amount: "))

if chosen_number < 65:
    discount = 0.2  
else:
    discount = 0.3 

discount_applied = total_purchase * discount
total_to_pay = total_purchase - discount_applied

print(f"Chosen number: {chosen_number}")
print(f"Discount applied: {discount_applied}")
print(f"Total to pay: {total_to_pay}")