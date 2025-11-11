import os
os.system("cls")

# Ejercicio 5 (versión alternativa) – Colores y emociones
# Pide al usuario su color favorito.
# Según el color, muestra un mensaje diferente.
# Por ejemplo:
# - Si elige "rojo", muestra "Eres una persona apasionada."
# - Si elige "azul", muestra "Eres tranquilo y reflexivo."
# - Si elige "verde", muestra "Te gusta la naturaleza."
# - Si elige otro color, muestra "Tienes un gusto único."

color = input("\n¿Cuál es su color favorito?: ")
if color.lower() == 'rojo':
    print("\nEres una persona apasionada")
elif color.lower() == 'azul':
    print("\nEres tranquilo y reflexivo")
elif color.lower() == 'verde':
    print("\nTe gusta la naturaleza")
else:
    print("\nTienes un gusto único")