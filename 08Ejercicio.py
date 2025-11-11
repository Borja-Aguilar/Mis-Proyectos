import os
os.system("cls")

# Ejercicio 8 – Año bisiesto
# Pide al usuario un año y muestra si es bisiesto o no.
# Un año es bisiesto si:
# - Es divisible entre 4 y no entre 100, o
# - Es divisible entre 400
# Ejemplo: 2000 y 2024 son bisiestos; 1900 y 2023 no lo son.

año = int(input("\nEscribe un año y te digo si es bisiesto: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("\nEs bisiesto")
else:
    print("\nNo es bisiesto")