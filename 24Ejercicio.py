import os
os.system("cls")

# 🧮 Ejercicio 24 — Promedio de tres notas
# Crea una función llamada promedio(n1, n2, n3) que reciba tres números
# y devuelva su promedio.
# Además, que la función devuelva un mensaje:
# - "Aprobado" si el promedio es mayor o igual a 5
# - "Reprobado" si el promedio es menor a 5
#
# Ejemplo:
# promedio(6, 7, 5) → "Aprobado"
# promedio(3, 4, 2) → "Reprobado"

def funcion ():
    n1 = int(input("\nEscriba un número: "))
    n2 = int(input("\nEscriba un número: "))
    n3 = int(input("\nEscriba un número: "))
    suma = (n1 + n2 + n3)
    promedio = (suma / 3)
    if promedio >= 5:
        print("\nEstas aprobado")
    else:
        print("\nEstas suspenso")
    return promedio
prom = funcion()
print ("\nCon una nota de:",prom)