import os
os.system("cls")
import re

# 📘 EJERCICIO 37
# Texto de ejemplo:
#texto = """
#El partido de fútbol se jugó el 12/09/2023 en el estadio central.
#Los espectadores incluían a Marta (30 años) y Luis (27 años).
#Los boletos fueron comprados a través de correo electrónico: reservas@futbol.com
#"""
# 1️⃣ Busca la primera fecha en el texto usando re.search()
# 2️⃣ Muestra si se encontró, su posición inicial y final
# 3️⃣ Usa re.IGNORECASE

text =  """
El partido de fútbol se jugó el 12/09/2023 en el estadio central.
Los espectadores incluían a Marta (30 años) y Luis (27 años).
Los boletos fueron comprados a través de correo electrónico: reservas@futbol.com
"""
pattern_fecha = r"\d{2}/\d{2}/\d{4}"
match = re.search(pattern_fecha, text)
if match:
    print("Primera fecha encontrada:", match.group())
    print("Empieza en:", match.start())
    print("Termina en:", match.end())
else:
    print("No se encontró ninguna fecha.")
