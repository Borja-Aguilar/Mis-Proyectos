import os
os.system("cls")

# 🧮 Ejercicio 25 — Contar números pares en una lista
# Crea una función llamada contar_pares(lista) que reciba una lista de números
# y devuelva cuántos son pares.
#
# Ejemplo:
# contar_pares([1, 2, 3, 4, 5, 6]) → 3
#
# 💡 Pista:
# - Usa un bucle for para recorrer la lista
# - Usa el operador % para comprobar si un número es par
# - Devuelve el conteo con return

def contar_pares():
    cont = 0
    lista = []
    for i in range(5):
        num = int(input(f"Escribe el número {i+1}: "))
        lista.append(num)
        if num % 2 == 0:
            cont += 1
    return cont, lista

cont, lista = contar_pares()
print("\nLos números introducidos son:", lista," de los cuales son pares:", cont)