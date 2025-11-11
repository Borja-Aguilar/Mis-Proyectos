import os
os.system("cls")
import sys

# Ejercicio 17 – Función para calcular el promedio
# Crea una función llamada 'promedio' que reciba una lista de números como argumento.
# La función debe calcular y devolver el promedio de los números.
# Luego, en el programa principal:
# 1. Pide al usuario que ingrese 5 números y guárdalos en una lista.
# 2. Llama a la función 'promedio' pasando la lista como argumento.
# 3. Muestra el resultado al usuario.
#
# Ejemplo de entrada:
# [4, 6, 8, 2, 10]
# Salida:
# El promedio de los números es: 6.0

def promedio(lista):
    suma = sum(lista)
    return suma / len(lista)

# Programa principal
lista = []
for i in range(5):
    num = int(input("Escribe un número: "))
    lista.append(num)

resultado = promedio(lista)
print("\nEl promedio de los números es:", resultado)
