import os
os.system("cls")

# 📘 EJERCICIO 34 — Gestión de contactos con diccionarios
# 1️⃣ Crea un diccionario llamado "agenda" que almacene contactos.
#     Cada contacto debe tener como clave su nombre y como valor otro diccionario
#     con la siguiente información:
#         - teléfono
#         - correo
# 2️⃣ Muestra todos los contactos usando un bucle for (nombre + datos).
# 3️⃣ Agrega un nuevo contacto a la agenda.
# 4️⃣ Modifica el teléfono de un contacto existente.
# 5️⃣ Elimina un contacto de la agenda usando .pop().
# 6️⃣ Muestra solo los nombres de los contactos usando .keys()
# 7️⃣ Muestra solo los correos usando .values()
# 8️⃣ Busca un nombre que el usuario ingrese y muestra su información
#     (si no existe, avisa).
# 9️⃣ Crea un diccionario llamado "agenda_extra" con al menos 2 contactos nuevos
#     y combínalo con la agenda original usando .update()
# 🔟 Muestra el diccionario final completo.
agenda = {
    "Borja": {
        "teléfono":"633 64 53 00",
        "correo":"borja@gmail.com"
    },
    "Alejandro": {
        "teléfono":"622 23 44 09",
        "correo":"alejando@gmail.com"
    },
    "Carmen": {
        "teléfono":"733 65 42 22",
        "correo":"carmen@gmail.com"
    },
}
for nombre, valor in agenda.items():
    print(nombre, valor)
agenda ["Manuel"] = {
    "teléfono":"773 54 33 34",
    "correo":"manuel@gmail.com"
}
agenda ["Alejandro"]["teléfono"] = "777 34 34 21"
agenda.pop("Carmen")
for nombre in agenda.keys():
    print(nombre)
for valor in agenda.values():
    print(valor["correo"])
nombre_buscar = input("Introduce el nombre a buscar: ")
if nombre_buscar in agenda:
    print("Información de", nombre_buscar)
    print("Teléfono:", agenda[nombre_buscar]["teléfono"])
    print("Correo:", agenda[nombre_buscar]["correo"])
else:
    print("Ese nombre no existe en la agenda.")
agenda_extra = {
    "Manolo": {
        "teléfono":"655 00 90 90",
        "correo":"manolo@gmail.com"
    },
    "Enrique": {
        "teléfono":"934 34 29 89",
        "correo":"enrique@gmail.com"
    },
}
agenda.update(agenda_extra)
for nombre, valor in agenda.items():
    print(nombre, valor)