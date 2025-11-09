import os
os.system("cls")

# Ejercicio 3 – Par o impar
# Pide al usuario que escriba un número y muestra si es par o impar.

numero = int(input("\nEscriba un número:"))
if numero % 2 == 0:
    print("\nEs par")
else:
    print("\nEs impar")