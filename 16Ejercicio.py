import os
os.system("cls")
import sys

# Ejercicio 16 – Filtrar números mayores que un valor
# Pide al usuario que ingrese 6 números enteros y guárdalos en una lista.
# Luego pide otro número llamado "límite".
# Usa comprensión de listas para crear una nueva lista que contenga
# solo los números que sean mayores que el "límite".
#
# Finalmente, muestra la lista original y la nueva lista filtrada.
#
# 💡 Ejemplo de salida:
# Lista original: [4, 8, 1, 10, 3, 7]
# Límite: 5
# Números mayores que el límite: [8, 10, 7]

num = []
lim = []
for i in range (6):
    numero = int(input("\nEscriba un número: "))
    num.append(numero)
limite = int(input("\nEscribe tu número límite: "))
for n in num:
    if n > limite:
        lim.append(n)
print("\nLa lista de todos los números que escribiste son: ", num,"\nEl límite era de: ",limite, "\nLos números que superan el límite son: ", lim)