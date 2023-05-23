"""""
Escriba un programa que permita adivinar un personaje de Marvel en base
a las tres preguntas siguientes:
a. ¿Puede volar?
b. ¿Es humano?
c. ¿Tiene máscara?
"""
skill1=input("can fly? yes/no: ")
skill2=input("is human? yes/no: ")
skill3=input("do you have a mask? yes/no: ")
if skill1.upper()=="yes" and skill2.upper()=="yes" and skill3.upper()=="no":
    print(f"is the bruja")
elif skill1.upper()=="no" and skill2.upper()=="yes" and skill3.upper()=="no":
    print(f"is hulk")
elif skill1.upper()=="yes" and skill2.upper()=="no" and skill3.upper()=="yes":
    print(f"is Thor")
else:
    print(f"character not found")
