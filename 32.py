"""
La oficina de incorporación del ejercito necesita un algoritmo que le
pueda permitir saber si un aspirante a ingresar a la institución como soldado es apto o no para poder vincularlo. Para que una persona sea apta, debe cumplir los siguientes requisitos:
a. Si es mujer, su estatura debe ser superior a 1.60 más y su edad debe
estar entre 20 y 25 años.
b. Si el aspirante es hombre, se estatura debe ser superior a 1.65 más y
su edad debe estar entre los 18 y 24 años.
c. Tanto mujeres como hombres deben ser solteros.
Diseñe el algoritmo de tal forma que permita informar si un aspirante es apto o no para ingresar al ejército."""

gender = input("Enter the applicant's gender (Female or Male): ")
height = float(input("Enter the applicant's height in meters: "))
age = int(input("Enter the applicant's age: "))
marital_status = input("Enter the applicant's marital status (Single): ")
if gender == "Female" or "female":
    if height > 1.60 and 20 <= age <= 25 and marital_status == "Single" or "single":
        print(f"Applicant is eligible to join the military.")
    else:
        print(f"Applicant does not meet the requirements to join the military.")
if gender == "Male" or "male":
    if height > 1.65 and 18 <= age <= 24 and marital_status == "Single" or "single":
        print(f"Applicant is eligible to join the army.")
    else:
        print(f"Applicant does not meet the requirements to join the military.")
else:
    print(f"Invalid gender. Please enter 'Female' or 'Male'.")