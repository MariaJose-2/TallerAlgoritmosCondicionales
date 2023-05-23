"""La empresa Auteco de motocicletas tiene una promoción de mitad de año,
que consiste en lo siguiente. Las motos marca Honda tienen un descuento
del 4%, las marcas Yamaha del 7% y las Suzuki del 15%, las otras marcas 3%."""

brand = input("Enter the brand of the motorcycle: ")
price = float(input("Enter the price of the motorcycle: "))
if brand.upper()=="honda":
    discount=price*0.04
    total=price-discount
elif brand=="yamaha":
    discount=price*0.07
    total=price-discount
elif brand=="suzuki":
    
    discount=price*0.15
    total=price-discount
else:
    discount=price*0.03
    total=price-discount
print(f"the discount is: {discount}")
print(f"the total is: {total}")
