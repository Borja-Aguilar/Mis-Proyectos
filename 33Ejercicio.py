import os
os.system("cls")

# 🎯 Ejercicio 33 — Gestión avanzada de inventario con diccionarios
#
# Vas a trabajar con un diccionario que representa el inventario de una tienda.
# 1️⃣ Crea un diccionario llamado inventario donde:
#     - La clave será el nombre del producto (str)
#     - El valor será otro diccionario con:
#           • "precio": precio del producto
#           • "stock": cantidad disponible
#     Ejemplo de estructura:
#     inventario = {
#         "Manzanas": {"precio": 1.5, "stock": 30},
#         "Pan": {"precio": 0.8, "stock": 12}
#     }
# 2️⃣ Muestra **todos los productos** con su precio y stock usando un for.
# 3️⃣ Agrega un nuevo producto al inventario pidiendo al usuario:
#       - Nombre del producto
#       - Precio
#       - Stock
# 4️⃣ Aumenta el stock de un producto ya existente.
#     (Elige tú qué producto y cuánto se suma)
# 5️⃣ Cambia el precio de un producto.
# 6️⃣ Elimina un producto del inventario usando .pop()
# 7️⃣ Muestra solo los nombres de los productos (claves)
# 8️⃣ Muestra solo los precios (recorriendo los valores)
# 9️⃣ Crea un segundo diccionario llamado inventario_extra con 2 productos nuevos.
# 🔟 Combina inventario con inventario_extra usando .update()
# 1️⃣1️⃣ Calcula el **valor total del inventario** sumando precio × stock de cada producto.
#      Muestra el resultado.
# 1️⃣2️⃣ Muestra el inventario final.
#
# 💡 Al final te debe quedar un diccionario de productos completamente actualizado.

inventario = {
    "Manzana":{"precio":1.5, "stock":30},
    "Pan":{"precio":0.8, "stock":12},
    "Sandia":{"precio":1.9, "stock":9},
    "Melón":{"precio":1.75, "stock":10},
    "Galletas":{"precio":2.3, "stock":6},
    "Chocolate":{"precio":0.99, "stock":5},
    "Muffins":{"precio":2.75, "stock":9},
}
inventario["Pan"]["precio"] = 0.99
inventario["Pan"]["stock"] = 11
inventario.pop("Sandia")
for nombre in inventario.keys():
    print(nombre)
for producto, info in inventario.items():
    print(info["precio"])
inventario_extra = {
    "Melocotón":{"precio":2.39, "stock":9},
    "Kiwi":{"precio":1.49, "stock":9},
}
inventario.update(inventario_extra)
total = 0
for producto, info in inventario.items():
    precio = info["precio"]
    stock = info["stock"]
    total += precio * stock
print(f" Valor total del inventario: {total} €")
print(inventario)

