import os
os.system("cls")
import sys

# Ejercicio 14 – Contar números positivos y negativos
# Pide al usuario que ingrese 7 números enteros y guárdalos en una lista.
# Recorre la lista y cuenta cuántos números son positivos y cuántos son negativos.
# Luego muestra los resultados:
# Ejemplo de salida:
# Números positivos: 4
# Números negativos: 3
# Nota: puedes usar un bucle for y condicionales if/else.

conpos = 0
conneg = 0
listanum = []
for i in range (7):
    num = int(input("\nEscriba números enteros, sean negativos o positivos: "))
    listanum.append(num)
    if num > 0:
        conpos += 1
    else:
        conneg += 1
print("\nEn total hay", conpos, "números positivos y", conneg ,"negativos")