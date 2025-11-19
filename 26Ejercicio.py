import os
os.system("cls")

# 🧩 Ejercicio 26 — Contar letras específicas
# Crea una función llamada contar_letra() que:
# 1. Pida al usuario que escriba una palabra o frase.
# 2. Pida también una letra que quiera buscar.
# 3. Cuente cuántas veces aparece esa letra en el texto.
# 4. Devuelva el número de veces.
#
# Ejemplo:
# Texto: "banana"
# Letra: "a"
# → Resultado: La letra 'a' aparece 3 veces.
#
# 💡 Pistas:
# - Usa .lower() para no tener problemas con mayúsculas/minúsculas.
# - Recorre el texto con un bucle for.
# - Usa un contador para sumar cuando la letra coincida.

def contar_letra():
    cont = 0
    palabra = input("\nEscriba lo que quiera: ")
    letra = input("\nEscriba una letra: ")
    for char in palabra:
        if char.lower() == letra.lower():
            cont += 1
    return palabra, letra, cont
palabra, letra, cont = contar_letra()
print("En lo escrito -->", palabra, " hay ",cont, " veces ",letra)