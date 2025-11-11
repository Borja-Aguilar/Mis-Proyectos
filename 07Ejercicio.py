import os
os.system("cls")

# Ejercicio 7 – El número mayor
# Pide al usuario tres números distintos y muestra cuál es el mayor.
# Si algunos son iguales, indícalo también.

num1 = int(input("\nEscribe el primer número: "))
num2 = int(input("\nEscribe el segundo número: "))
num3 = int(input("\nEscribe el tercer número: "))

if num1 == num2 == num3:
    print("\nLos tres números son iguales")
elif num1 >= num2 and num1 >= num3:
    print(f"\nEl número mayor es {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"\nEl número mayor es {num2}")
else:
    print(f"\nEl número mayor es {num3}")

