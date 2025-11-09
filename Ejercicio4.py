import os
os.system("cls")

# Ejercicio 4 – Nota escolar
# Pide al usuario una nota del 0 al 10 y muestra:
# - "Suspenso" si es menor de 5
# - "Aprobado" si es 5 o 6
# - "Notable" si es 7 u 8
# - "Sobresaliente" si es 9 o 10

nota = float(input("\nEscriba la nota que obtuviste:"))
if nota >= 9:
    print("\nSobresaliente")
elif nota >= 7:
    print("\nNotable")
elif nota >= 5:
    print("\nAprobado")
else:
    print("\nSuspenso")