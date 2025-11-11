import os
os.system("cls")

# Ejercicio 6 – Derecho a votar
# Pide al usuario su edad y su nacionalidad.
# Si tiene 18 años o más **y** su nacionalidad es "española",
# muestra "Puedes votar en España".
# En caso contrario, muestra "No puedes votar en España".

edad = int(input("\n¿Cuántos años tienes?:"))
pais = input("Nacionalidad= ")
if edad >= 18 and pais.lower() == 'españa':
    print("\nPuedes votar en España")
else:
    print("\nNo puedes votar en España")