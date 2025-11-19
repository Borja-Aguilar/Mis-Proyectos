import os
os.system("cls")

# 🎯 Ejercicio 30 — Contar números positivos, negativos y ceros

# Crea una función llamada contar_positivos_negativos_ceros() que:
# 1️⃣ Pida al usuario que ingrese 7 números (uno por uno).
# 2️⃣ Guarde todos los números en una lista.
# 3️⃣ Guarde en otra lista solo los números positivos.
# 4️⃣ Guarde en otra lista solo los números negativos.
# 5️⃣ Guarde en otra lista los ceros.
# 6️⃣ Cuente cuántos positivos, negativos y ceros hay.
# 7️⃣ Devuelva las cuatro listas y los contadores.
# 8️⃣ Finalmente, muestra el resultado con print().

def contar_positivos_negativos_ceros():
    lista1 = []
    pos = []
    neg = []
    ceros = []
    contpos = 0
    contneg = 0
    contceros = 0
    for i in range(7):
        num = int(input(f"\nEscriba el número {i+1}: "))
        lista1.append(num)
        if num > 0:
            pos.append(num)
            contpos = len(pos)
        elif num == 0:
            ceros.append(num)
            contceros = len(ceros)
        else:
            neg.append(num)
            contneg = len(neg)
    return lista1, pos, neg, ceros, contpos, contneg, contceros
lista1, pos, neg, ceros, contpos, contneg, contceros = contar_positivos_negativos_ceros()
print(f"\nLos números introducidos son {lista1}, positivos son {pos}, negativos {neg} y hay una cantidad de números positivos de {contpos}, de negativos {contneg} y de ceros {contceros}")

        
