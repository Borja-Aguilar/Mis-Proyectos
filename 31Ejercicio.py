import os
os.system("cls")

# 🎯 Ejercicio 31 — Análisis mixto de texto, números y diccionarios

# Crea una función llamada analisis_mixto() que haga lo siguiente:

# 🧩 PARTE 1 — TEXTO
# 1️⃣ Pida al usuario que escriba una frase.
# 2️⃣ Cuente cuántas letras "r" y "j" hay en el texto.
# 3️⃣ Muestra si el texto está "balanceado" (si tiene la misma cantidad de "r" y "j").

# 🔢 PARTE 2 — NÚMEROS
# 4️⃣ Pida al usuario que ingrese 5 números (uno por uno) y guárdalos en una lista.
# 5️⃣ Pida también un número meta (goal).
# 6️⃣ Busca dentro de la lista qué dos números suman el goal.
# 7️⃣ Si existen, muéstralos; si no, muestra un mensaje diciendo que no se encontró pareja.

# 🦖 PARTE 3 — DICCIONARIO
# 8️⃣ Crea un diccionario llamado info con la siguiente información:
#       {"texto": <frase_ingresada>, "numeros": <lista>, "goal": <valor_goal>}
# 9️⃣ Añade una nueva clave llamada "resultado" con el par de números encontrados (o None si no hay).
# 🔟 Muestra todas las claves y valores del diccionario usando un for con .items().
# 1️⃣1️⃣ Elimina la clave "goal" del diccionario con .pop() y muestra el resultado final.
# 1️⃣2️⃣ Finalmente, devuelve el diccionario modificado.

# 💡 Pista:
# - Usa text.count("r") y text.count("j") para contar letras.
# - Usa for i in range(len(lista)) y for j in range(i+1, len(lista)) para buscar pares.
# - Usa .items(), .update() y .pop() en el diccionario.

def analisis_mixto():
    texto = input("Escribe qué hiciste en tu último verano: ")
    text_upper = texto.upper()
    count_r = text_upper.count("R")
    count_j = text_upper.count("J")
    print(f"\nCantidad de 'R': {count_r}, Cantidad de 'J': {count_j}")
    balanceado = (count_r == count_j)
    if balanceado:
        print("El texto está balanceado.")
    else:
        print("El texto NO está balanceado.")

    lista = []
    for i in range(5):
        num = int(input(f"\nEscribe el número {i+1}: "))
        lista.append(num)
    goal = int(input("\nEscribe el número considerado goal: "))
    vistos = {}
    pareja = None

    for index, value in enumerate(lista):
        falta = goal - value 
        if falta in vistos:
            pareja = (falta, value)
            print(f"\nPareja encontrada: {falta} + {value} = {goal}")
            break
        vistos[value] = index
    if pareja is None:
        print("\nNo se encontró ninguna pareja que sume el goal.")

    info = {
        "texto": texto,
        "cantidad_R": count_r,
        "cantidad_J": count_j,
        "balanceado": balanceado,
        "numeros": lista,
        "goal": goal,
        "resultado": pareja
    }
    print("\n--- DICCIONARIO COMPLETO ---")
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

    eliminado = info.pop("goal")
    print(f"\nSe eliminó 'goal' cuyo valor era: {eliminado}")

    print("\n--- DICCIONARIO FINAL (sin 'goal') ---")
    for clave, valor in info.items():
        print(f"{clave}: {valor}")
    return info
analisis_mixto()