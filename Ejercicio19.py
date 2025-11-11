import os
os.system("cls")
import sys

# Ejercicio 19 – Cuadrado y cubo de números
# 1. Crea una función que pida al usuario 5 números enteros y los guarde en una lista.
# 2. Crea otra función que reciba esa lista como argumento.
# 3. La segunda función debe calcular para cada número:
#    - su cuadrado
#    - su cubo
# 4. Muestra los resultados en pantalla con mensajes claros,
#    indicando qué número es, su cuadrado y su cubo.

def numeros():
    lista = []
    cuadrados = []
    cubos = []

    for i in range(5):

        while True:
            try:
                num = int(input(f"Escriba el número {i+1}: "))
                break
            except ValueError:
                print("Entrada no válida. Introduce un número entero.")

        lista.append(num)
        cuadrados.append(num ** 2)
        cubos.append(num ** 3)

        print(f"El número {num} → Cuadrado: {num ** 2} | Cubo: {num ** 3}")

    print("\nResumen final:")
    for idx in range(len(lista)):
        print(f"{idx+1}) {lista[idx]} -> cuadrado: {cuadrados[idx]}, cubo: {cubos[idx]}")

    return lista, cuadrados, cubos

if __name__ == "__main__":
    numeros()
