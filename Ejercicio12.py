import os
os.system("cls")
import sys

# Ejercicio 12 – Filtrar números mayores que la media
# Pide al usuario que ingrese 5 números y guárdalos en una lista.
# Calcula la media (promedio) de esos números.
# Luego muestra únicamente los números que sean mayores que la media.
# Usa un bucle for para recorrer la lista y condicionales if.
# (Pista: también puedes intentar hacerlo con una lista por comprensión para practicar)
# Ejemplo:
# Entrada -> [4, 6, 8, 2, 10]
# Media -> 6
# Números mayores que la media -> [8, 10]

cont = 0
suma = 0
media = 0
lista1 = []
for i in range(5):
    num = int(input("Escribe un número: "))
    lista1.append(num)
    suma += num
    cont += 1
media = suma / cont
for n in lista1:
    if n > media:
        print(n, "es mayor que la media, y la media es de: ", media)

