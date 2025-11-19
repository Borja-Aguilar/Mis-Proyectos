import os
os.system("cls")

# 🎯 Ejercicio 29 — Contar números pares e impares
# Crea una función llamada contar_pares_impares() que:
# 1️⃣ Pida al usuario que introduzca 5 números (uno por uno).
# 2️⃣ Guarde todos los números en una lista.
# 3️⃣ Cuente cuántos son pares y cuántos son impares.
# 4️⃣ Devuelva ambos resultados.
# 5️⃣ Finalmente, muestra en pantalla los números introducidos y los totales.
#
# 💡 Pistas:
# - Un número es par si num % 2 == 0
# - Usa un bucle for y un contador para cada tipo.
#
# 🔹 Ejemplo:
# Escribe el número 1: 2
# Escribe el número 2: 7
# Escribe el número 3: 4
# Escribe el número 4: 5
# Escribe el número 5: 10
#
# → Números introducidos: [2, 7, 4, 5, 10]
# → Pares: 3
# → Impares: 2

def contar_pares_impares():
    lista = []
    pares = []
    impar = []
    for i in range(5):
        num = int(input(f"\nEscribe el número {i+1} : "))
        lista.append(num)
        if num % 2 == 0:
            pares.append(num)
        else:
            impar.append(num)
    return lista, pares, impar
lista, pares, impar = contar_pares_impares()
print(f"\nLos números introducidos son {lista}, números pares son {pares} e impares {impar}")