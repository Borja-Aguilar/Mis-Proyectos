import os
os.system("cls")

# 🎯 Ejercicio 27 — Adivina la palabra secreta
# Crea una función llamada adivinar_palabra() que:
# 1. Tenga guardada una palabra secreta dentro de la función.
# 2. Pida al usuario que intente adivinarla.
# 3. Mientras el usuario no acierte, el programa debe decir:
#    "Incorrecto, intenta de nuevo."
# 4. Cuando acierte, debe decir:
#    "¡Muy bien! Adivinaste la palabra."
#
# 💡 Pistas:
# - Usa un bucle while para repetir hasta que acierte.
# - Convierte todo a minúsculas con .lower() para no tener problemas.
# - No hace falta usar return en este caso.
#
# Ejemplo:
# Palabra secreta: "python"
# Usuario escribe: "java" → "Incorrecto"
# Usuario escribe: "python" → "¡Muy bien! Adivinaste la palabra."

def adivinar_palabra():
    secreto = 'palabra'
    palabra = ""
    while palabra != secreto:
        palabra = input("\nIntenta adivinarla: ")
        if palabra != secreto:
            print("\nIncorrecto, intenta de nuevo.")
    
    print("¡Muy bien! Adivinaste la palabra.")

adivinar_palabra()