import os
os.system("cls")
import sys

# Ejercicio 20 – Contar vocales y consonantes en una palabra

# 1. Crea una función que pida al usuario una palabra.
# 2. Crea otra función que reciba esa palabra como argumento.
# 3. La segunda función debe contar cuántas vocales y cuántas consonantes tiene la palabra.
# 4. Muestra los resultados con mensajes claros indicando:
#    - La palabra que escribiste
#    - Número de vocales
#    - Número de consonantes

# 🔹 Pistas:
# - Considera que la palabra puede tener letras mayúsculas o minúsculas.
# - Puedes usar 'for letra in palabra:' para recorrer la palabra letra por letra.
# - Las vocales son: a, e, i, o, u

def pedir_palabra():
    palabra = input("\nEscribe una palabra: ")
    return palabra

def contar_letras(palabra):
    vocales = "aeiouAEIOU"
    num_vocales = 0
    num_consonantes = 0

    for letra in palabra:
        if letra.isalpha():
            if letra in vocales:
                num_vocales += 1
            else:
                num_consonantes += 1

    print(f"\nPalabra: {palabra}")
    print(f"Número de vocales: {num_vocales}")
    print(f"Número de consonantes: {num_consonantes}")

if __name__ == "__main__":
    palabra_usuario = pedir_palabra()       
    contar_letras(palabra_usuario)        


