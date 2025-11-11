import os
os.system("cls")

# Ejercicio 2 – Comparar dos números
# Pide al usuario que escriba dos números y muestra cuál es mayor o si son iguales.

num1 = int(input("\nEscribe el primer número: "))
num2 = int(input("\nEscriba el segundo número: "))
if num1 > num2:
    print(num1, "es mayor que", num2)
else:
    if num1 < num2:
        print(num1, "es menor que", num2)
    else:
        print(num1, "es igual que", num2)
