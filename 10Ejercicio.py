import os
os.system("cls")
import sys

# Ejercicio 10 – Suma de números pares
# Instrucciones:
# 1. Pide al usuario que ingrese 5 números enteros, uno por uno.
# 2. Almacena los números en una lista para poder trabajar con ellos.
# 3. Recorre la lista y selecciona solo los números que sean pares (divisibles entre 2).
# 4. Suma todos los números pares que encontraste.
# 5. Muestra el resultado final al usuario con un mensaje claro, por ejemplo:
#    "La suma de los números pares es: X"

lista1 = []
suma = 0
for i in range(5):
    num = int(input("\nEscribe un número entero:"))
    if num % 2 == 0:
        suma += num
    else:
        pass
lista1.append(suma)
print("\nLa suma total de los números pares es de: ", lista1)