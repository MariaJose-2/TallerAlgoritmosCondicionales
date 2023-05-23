"""""
Escriba un programa en Python que acepte la opción de dos jugadoras en
a. Piedra-Papel-Tijera y decida el resultado (solución).
b. Entrada: persona1=piedra; persona2=papel
c. Salida: Gana persona2: El papel envuelve a la piedra
"""
player1=input("Write your answer: Paper(p) Rock(r) Scissors(s) \n")
player2=input("Write your answer: Paper(p) Rock(r) Scissors(s) \n")
if player1.upper()=="p" and player2.upper()=="r":
    print(f"gplayer one wins")
elif player1.upper()=="p" and player2.upper()=="s":
    print(f"player two wins")
elif player1.upper()=="s" and player2.upper()=="p":
    print(f"player one wins")
elif player1.upper()=="p" and player2.upper()=="r":
    print(f"player one wins") 
elif player1.upper()=="r" and player2.upper()=="s":
    print(f"player two wins")
    