import os
os.system("cls")
import sys

# 🔢 Ejercicio 22 — Suma de dos números
# Escribe una función llamada sumar(a, b) que reciba dos números
# y devuelva su suma.
# Después, llama a la función con distintos valores y muestra el resultado con print().
# Ejemplo:
# sumar(3, 5) → 8

def suma ():
    numero1 = int(input("Escriba un número: "))
    numero2 = int(input("\nEscriba un segundo número: "))
    suma = numero1 + numero2
    return suma
print(suma())