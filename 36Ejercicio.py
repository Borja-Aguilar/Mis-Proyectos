import os
os.system("cls")
import re

# 📘 EJERCICIO 36 — Extracción de información con expresiones regulares
# 📝 TEXTO PARA ANALIZAR (lo doy yo, NO se pide por input)
#texto = """
#El pasado verano viajé a Madrid el día 12/07/2023 y más tarde estuve en Valencia el 25/08/2023.
#Allí conocí a varias personas, como Ana (23 años), Marcos (31 años) y Laura (27 años).
#También anoté algunos teléfonos: 633-245-889, 722-90-44-12 y 900-123-456.
#Además envié correos a: contacto@gmail.com, info_empresa@negocio.es y test123@correo.org
#"""
# 1️⃣ Busca y muestra todas las fechas con formato dd/mm/yyyy usando re.findall()
# 2️⃣ Busca todos los números de teléfono del texto (formatos XX-XXX-XXX o XXX-XXX-XXX)
# 3️⃣ Encuentra todos los correos electrónicos usando una expresión regular.
# 4️⃣ Localiza todas las edades (números seguidos de la palabra "años")
# 5️⃣ Crea un diccionario llamado "resultado" donde almacenes:
#       - "fechas": lista con todas las fechas
#       - "telefonos": lista con teléfonos encontrados
#       - "emails": lista con los correos
#       - "edades": lista de edades encontradas
# 6️⃣ Muestra el diccionario final.

text = """
El pasado verano viajé a Madrid el día 12/07/2023 y más tarde estuve en Valencia el 25/08/2023.
Allí conocí a varias personas, como Ana (23 años), Marcos (31 años) y Laura (27 años).
También anoté algunos teléfonos: 633-245-889, 722-90-44-12 y 900-123-456.
Además envié correos a: contacto@gmail.com, info_empresa@negocio.es y test123@correo.org
"""
pattern_fechas = r"\d{2}/\d{2}/\d{4}"
fechas = re.findall(pattern_fechas, texto)
pattern_telefonos = r"\d{2,3}(?:-\d{2,3}){2,3}"
telefonos = re.findall(pattern_telefonos, texto)
pattern_emails = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(pattern_emails, texto)
pattern_edades = r"\d{1,2}\s*años"
edades = re.findall(pattern_edades, texto)
resultado = {
    "fechas": fechas,
    "telefonos": telefonos,
    "emails": emails,
    "edades": edades
}
print("\n Diccionario con toda la información extraída:")
for clave, valor in resultado.items():
    print(f"{clave}: {valor}")
print("\n Cantidad de elementos en cada categoría:")
for clave, valor in resultado.items():
    print(f"{clave}: {len(valor)}")
