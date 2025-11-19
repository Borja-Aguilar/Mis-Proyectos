import os
os.system("cls")

# 🎯 Ejercicio 32 — Practicando diccionarios
# 1️⃣ Crea un diccionario llamado 'estudiantes' con 5 nombres de estudiantes como claves 
#     y sus edades como valores.
# 2️⃣ Muestra todos los estudiantes con su edad usando un bucle.
# 3️⃣ Modifica la edad de uno de los estudiantes.
# 4️⃣ Agrega un nuevo estudiante con su edad al diccionario.
# 5️⃣ Elimina a un estudiante usando su nombre.
# 6️⃣ Comprueba si un estudiante existe en el diccionario y muestra un mensaje.
# 7️⃣ Muestra solo los nombres de los estudiantes usando .keys().
# 8️⃣ Muestra solo las edades de los estudiantes usando .values().
# 9️⃣ Crea un diccionario nuevo combinando los datos del diccionario original
#     con otro diccionario de estudiantes extra usando .update().

estudiantes = {
    "Borja":19,
    "Triana":20,
    "Hugo":14,
    "Manolo":23,
    "Lucia":32,
}
for nombre, edad in estudiantes.items():
    print(nombre, edad)
estudiantes["Triana"] = 15
estudiantes["Antonio"] = 20
estudiantes.pop("Borja")
for nombre, edad in estudiantes.items():
    print(nombre, edad)
for nombre in estudiantes.keys():
    print(nombre)
for edad in estudiantes.values():
    print(edad)
extra = {
    "Enrique":14,
    "Martina":16,
    "Eusebio":33
}
estudiantes.update(extra)
print(estudiantes)