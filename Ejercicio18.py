import os
os.system("cls")
import sys

# Ejercicio 18 – Función para contar números positivos y negativos
# Crea una función llamada 'contar_positivos_negativos' que:
# 1. Pida al usuario que ingrese 6 números enteros y los guarde en una lista.
# 2. Recorra la lista y cuente cuántos números son positivos y cuántos negativos.
# 3. Devuelva ambos conteos (positivos y negativos) al programa principal.
#
# Luego, en el programa principal:
# - Llama a la función y muestra los resultados.
#
# Ejemplo de salida:
# Números positivos: 4
# Números negativos: 2

def contar_positivos_negativos():
    lista = []        
    positivos = []     
    negativos = [] 

    for i in range(6):
        num = int(input(f"Escribe el número {i+1}: "))
        lista.append(num)  

        if num >= 0:
            positivos.append(num)
        else:
            negativos.append(num)

    print("\nLista completa:", lista)
    print("Números positivos:", positivos)
    print("Números negativos:", negativos)

contar_positivos_negativos()
