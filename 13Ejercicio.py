import os
os.system("cls")
import sys

# Ejercicio 13 – Combinaciones de letras y números
# Pide al usuario que ingrese 3 letras y 3 números.
# Guarda las letras en una lista y los números en otra.
# Luego muestra todas las combinaciones posibles de letra + número usando un bucle for anidado.
# Ejemplo:
# Letras: ['A', 'B', 'C']
# Números: [1, 2, 3]
# Salida:
# A1
# A2
# A3
# B1
# B2
# B3
# C1
# C2
# C3

letras = []
numeros = []
for i in range (3):
    num = int(input("\nEscribe un número: "))
    numeros.append(num)
    let = input("\nEscribe una letra: ")
    letras.append(let)

for letra in letras:
    for numero in numeros:
        print(letra, numero)