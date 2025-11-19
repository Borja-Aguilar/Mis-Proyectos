import os
os.system("cls")

# 📘 EJERCICIO 35 — Registro de alumnos y notas
# 1️⃣ Crea un diccionario llamado "alumnos" que almacene 5 alumnos.
#     Cada alumno será una clave (su nombre) y el valor será otro diccionario con:
#         - "edad"
#         - "notas": una lista con al menos 3 calificaciones
# 2️⃣ Muestra todos los alumnos con su edad y sus notas usando un bucle for.
# 3️⃣ Calcula la nota media de cada alumno y añádela como un nuevo campo "media" en su diccionario.
# 4️⃣ Modifica la edad de un alumno específico.
# 5️⃣ Agrega un nuevo alumno con sus datos al diccionario.
# 6️⃣ Elimina un alumno usando .pop().
# 7️⃣ Muestra solo los nombres de los alumnos usando .keys().
# 8️⃣ Muestra solo las medias de todos los alumnos recorriendo los diccionarios internos.
# 9️⃣ Crea otro diccionario "alumnos_extra" con al menos 2 alumnos nuevos y combínalo con el diccionario original usando .update().
# 🔟 Muestra el diccionario final completo con todos los alumnos y sus datos.

alumnos = {
    "Borja": {
        "edad": 19,
        "notas": [7, 8.5, 9]
    },
    "Lucía": {
        "edad": 18,
        "notas": [9, 7.5, 8]
    },
    "Alejandro": {
        "edad": 20,
        "notas": [6, 5.5, 7]
    },
    "Carmen": {
        "edad": 19,
        "notas": [8, 8, 8]
    },
    "Manuel": {
        "edad": 21,
        "notas": [10, 9.5, 9]
    },
}
print("\n LISTA DE ALUMNOS:")
for nombre, datos in alumnos.items():
    print(nombre, datos)
for nombre, datos in alumnos.items():
    notas = datos["notas"]
    media = sum(notas) / len(notas)
    datos["media"] = round(media, 2)
print("\n ALUMNOS CON MEDIA AÑADIDA:")
for nombre, datos in alumnos.items():
    print(nombre, datos)
alumnos["Borja"]["edad"] = 20
alumnos["Sofía"] = {
    "edad": 22,
    "notas": [9, 8, 9],
}
alumnos["Sofía"]["media"] = sum(alumnos["Sofía"]["notas"]) / len(alumnos["Sofía"]["notas"])
alumnos.pop("Carmen")
print("\n SOLO NOMBRES:")
for nombre in alumnos.keys():
    print(nombre)
print("\n MEDIAS DE LOS ALUMNOS:")
for datos in alumnos.values():
    print(datos["media"])
alumnos_extra = {
    "Manolo": {
        "edad": 23,
        "notas": [6, 7, 6],
    },
    "Enrique": {
        "edad": 24,
        "notas": [9, 9, 10],
    }
}
for nombre, datos in alumnos_extra.items():
    datos["media"] = sum(datos["notas"]) / len(datos["notas"])
alumnos.update(alumnos_extra)
print("\n DICCIONARIO FINAL:")
for nombre, datos in alumnos.items():
    print(nombre, datos)

