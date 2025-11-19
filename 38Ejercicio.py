import os
os.system("cls")
import re

# 📘 EJERCICIO 38
# Texto de ejemplo:
texto = """
Contactos de emergencia: ana.sanchez@mail.com, pedro.lopez@empresa.org, soporte@web.net.
Por favor, envía un mensaje a todos para confirmar la reunión.
"""
# 1️⃣ Usa re.finditer() para encontrar todos los emails
# 2️⃣ Muestra cada email y su posición de inicio y fin en el texto

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
print(" Emails encontrados en el texto:")
for match in re.finditer(pattern, texto):
    print("Email:", match.group(), "Empieza en:", match.start(), "Termina en:", match.end())