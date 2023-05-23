"""Se debe validar tres atajos de visual estudio code si cumple los tres, deberá
informar al usuario que felicidades es correcto de lo contrario debe indicar
que no aplica."""
shortcut1 = input("Enter the first Visual Studio Code shortcut: ")
shortcut2 = input("Enter the second Visual Studio Code shortcut: ")
shortcut3 = input("Enter the third Visual Studio Code shortcut: ")

if shortcut1 == "CTRL+K+C" or "ctrl+k+c" and shortcut2 == "CTRL+Z" or "ctrl+z" and shortcut3 == "Ctrl+S" or "ctrl+s" :
    print(f"congratulations is correct")
else:
    print(f"Not applicable.")
