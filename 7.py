"""Diseñe un algoritmo que lea el nombre del estudiante, el valor de su matrícula en un curso que responda si¿ Es egresado de la universidad?, si la respuesta es SI, se le aplica un 30 % descuento. Muestre el nombre del estudiante y el valor de la matricula a pagar."""

studentName = input("Enter student's name: ")
tuitionValue = float(input("enter the tuition fee: "))
is_graduated = input("Are you a college graduate? (yes/no): ")
if is_graduated.upper() == "yes":
    discount = 0.3 
else:
    discount = 0
amount_to_be_paid = tuitionValue - (tuitionValue * discount)

print(f"Student name: {studentName}")
print(f"tuition value to pay: {amount_to_be_paid}")