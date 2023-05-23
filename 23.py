"""
Un cliente va a comprar una moto y se percata que si lo compraba el día
martes tiene un descuento del 10%, luego si lo compra el día sábado tiene
un descuento del 18% mostrar cuanto pagara en cada opción.
"""
day_of_week = input("Enter the day of the week(tuesday and saturday):")
price = float(input("Enter the price of the motorcycle: "))
discount=0
if day_of_week.lower() == "tuesday":
    discount=price*0.1  
    total=price-discount
elif day_of_week.lower() == "saturday":
    discount=price*0.18  
    total=price-discount
total=price-discount
print(f"the total to pay is:{total}")
