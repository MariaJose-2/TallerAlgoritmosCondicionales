"""Hacer un algoritmo que calcule el total a pagar por la compra de camisas.
Si se compran tres camisas o más se aplica un descuento del 15% sobre el
total de la compra y si son menos de 3 camisas el descuento es del 5%."""

shirt_quantity = int(input("Enter the quantity of shirts purchased: "))
shirt_price = float(input("Enter the price of each shirt: "))

subtotal = shirt_quantity * shirt_price

if shirt_quantity >= 3:
    discount = subtotal * 0.15
else:
    discount = subtotal * 0.05

total_payment = subtotal - discount

print(f"The total payment for the shirt purchase is: {total_payment}")
