""""
La tienda sofia valida el valor de la compra si el valor de la compra es mayor
a 40 mil , si es así debe indicar el color de la balota(roja 10%, blanca 15%,
negra 20%,amarilla 20%, verde 30%) según el color se aplica el descuento, se
debe mostrar el descuento y el valor neto a pagar.
Si los valores son menores que 40 no va aplicar ningún descuento.
"""
purchasePrice=float(input("enter the value of the purchase"))
if purchasePrice > 40000:
    ballot_color = input("Enter the color of the ballot (red, white, black, yellow or green): ")

    if ballot_color == "red":
        discount = purchasePrice * 0.1
    if ballot_color == "white":
        discount = purchasePrice * 0.15
    elif ballot_color == "black" or ballot_color == "yellow":
        discount = purchasePrice * 0.2
    elif ballot_color == "green":
        discount = purchasePrice * 0.3
    else:
        print(f"Invalid ballot color.")
        discount = 0

    net_value = purchasePrice- discount
    print(f"Discount applied: ${discount}")
    print(f"Net value to be paid: $ {net_value}")
else:
    print(f"Purchase value is not greater than 40,000. no discount is applied.")