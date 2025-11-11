import os
os.system("cls")
import sys


# Ejercicio 11 – Buscar una letra en una palabra
# Pide al usuario que escriba una palabra.
# Luego pide una letra y muestra cuántas veces aparece en esa palabra.
# Si no aparece, muestra un mensaje indicando que la letra no está.
# Usa un bucle for para recorrer la palabra y un contador.
# (Pista: puedes usar un for con 'in' para recorrer cada carácter de la cadena)

cont = 0
palabra = input("Escriba una palabra ")
letra = input("Escriba una letra ")
for letter in palabra:
    if letter == letra:
        cont += 1
    else:
        pass
if cont == 0:
    print("No hay", letra, "en la palabra", palabra,)
else:
    print("Contiene la letra:", letra, cont,"veces")