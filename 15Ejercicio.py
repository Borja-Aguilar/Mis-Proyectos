import os
os.system("cls")
import sys

# Ejercicio 15 – Separar números pares e impares
# Pide al usuario que ingrese 8 números enteros y guárdalos en una lista.
# Luego recorre la lista y separa los números pares e impares en dos listas distintas:
#   - Una lista llamada "pares"
#   - Otra llamada "impares"
#
# Al final, muestra ambas listas por pantalla.
# Usando comprensión de listas
#
# Ejemplo de salida:
# Lista original: [3, 8, 5, 2, 9, 10, 12, 7]
# Pares: [8, 2, 10, 12]
# Impares: [3, 5, 9, 7]

num = []
pares = []
impar = []
for i in range (8):
    numero = int(input("Escribe un número: "))
    num.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impar.append(numero)

print("\nLa lista de números introducidos son: ", num,"\nde los cuales, son pares: ", pares,"\ne impares:", impar)