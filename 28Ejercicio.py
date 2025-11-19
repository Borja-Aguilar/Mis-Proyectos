import os
os.system("cls")

# 🎯 Ejercicio 28 — Contar cuántas palabras hay en una frase
# Crea una función llamada contar_palabras() que:
# 1️⃣ Pida al usuario que escriba una frase completa.
# 2️⃣ Cuente cuántas palabras tiene (separadas por espacios).
# 3️⃣ Devuelva el número total de palabras.
# 4️⃣ Finalmente, muestra el resultado con un print.
#
# 💡 Pistas:
# - Usa el método .split() para dividir la frase en palabras.
# - Puedes usar len() para contar cuántas hay.
#
# 🔹 Ejemplo:
# Escribe una frase: Hola que tal estás
# → La frase tiene 4 palabras.

def contar_palabras():
    frase = input("Escriba una frase completa --> ")
    palabras = frase.split()
    total = len(palabras)
    return total
total = contar_palabras()
print(f"\nEn la frase hay {total} palabras")