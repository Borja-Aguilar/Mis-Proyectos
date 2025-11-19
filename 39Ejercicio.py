import os
os.system("cls")
import re

# 📘 EJERCICIO 39 — Contar vocales en un texto
# Enunciado:
# 1️⃣ Se proporciona un texto.
# 2️⃣ Cuenta cuántas veces aparece cada vocal (a, e, i, o, u) en el texto, sin distinguir mayúsculas de minúsculas.
# 3️⃣ Guarda los resultados en un diccionario y muéstralo.

# Texto de ejemplo
texto = """
Python es un lenguaje de programación muy popular.
Es usado para desarrollo web, ciencia de datos, inteligencia artificial y automatización.
Aprender Python es divertido y útil para la carrera profesional.
"""
vocales = "aeiou"
contador = {}
for vocal in vocales:
    contador[vocal] = len(re.findall(vocal, texto, re.IGNORECASE))
print(" Conteo de vocales en el texto:")
for vocal, cantidad in contador.items():
    print(f"{vocal}: {cantidad}")
