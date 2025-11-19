import os
os.system("cls")

# 🧮 Ejercicio 23 — Número mayor
# Crea una función llamada mayor(a, b) que reciba dos números
# y devuelva el mayor de los dos.
#
# Ejemplo:
# mayor(10, 3) → 10
# mayor(4, 9) → 9
#
# 💡 Pista: usa una estructura if dentro de la función.

def mayor():
    numeroa = int(input("\nEscribe un número: "))
    numerob = int(input("\nEscribe un número: "))
    if numeroa < numerob:
        print(numeroa," es menor a ",numerob)
    elif numerob < numeroa:
        print(numeroa," es mayor a ",numerob)
    else:
        print(numeroa," es igual a ",numerob)
    return numeroa,numerob
mayor()