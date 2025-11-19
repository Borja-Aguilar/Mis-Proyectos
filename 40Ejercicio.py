import os
os.system("cls")
import re

# 📘 EJERCICIO 40 — Contar palabras en un texto
# Enunciado:
# 1️⃣ Se proporciona un texto.
# 2️⃣ Crea un diccionario donde:
#    - Clave: palabra del texto (sin signos de puntuación)
#    - Valor: número de veces que aparece
# 3️⃣ Muestra las 5 palabras más frecuentes en el texto.
# 4️⃣ Ignora mayúsculas/minúsculas al contar.
# Texto de ejemplo
texto = """
La biblioteca central tiene miles de libros sobre historia, ciencia y arte.
Cada estudiante puede sacar hasta cinco libros por semana.
Además, hay actividades educativas y talleres de lectura para todas las edades.
"""
palabras = re.findall(r"\b\w+\b", texto, re.IGNORECASE)
conteo = {}
for palabra in palabras:
    palabra_lower = palabra.lower()
    if palabra_lower in conteo:
        conteo[palabra_lower] += 1
    else:
        conteo[palabra_lower] = 1
print(" Conteo de todas las palabras:")
for palabra, cantidad in conteo.items():
    print(f"{palabra}: {cantidad}")
top5 = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:5]
print("\n Top 5 palabras más frecuentes:")
for palabra, cantidad in top5:
    print(f"{palabra}: {cantidad}")
