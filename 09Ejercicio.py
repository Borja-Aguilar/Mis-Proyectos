import os
os.system("cls")
import sys

# Ejercicio 9 – Notas, media y mensaje
# Pide al usuario tres notas de un estudiante.
# Calcula si aprueba todas (nota >= 5 cada una).
# Calcula la media de las notas.
# Si aprueba todas, muestra "El alumno aprueba todas"
#   y dependiendo de la media:
#   - media >= 9: "¡Felicidades, excelente trabajo!"
#   - media >= 7: "Buen trabajo, sigue así"
#   - media < 7: "Has aprobado, pero puedes mejorar"
# Si no aprueba todas, muestra "El alumno no aprueba todas"

dividir = 3
notato = 0
for i in range(3):
    nota = float(input("\nEscribe tu nota:"))
    if nota >= 5:
        notato = notato + nota
    else:
        print("\nTienes que recuperar")
        sys.exit()
total = (notato / dividir)
print("Tu nota media es de:", total)
if total >= 9:
    print("¡Felicidades, excelente trabajo!")
elif total >= 7:
    print("Buen trabajo, sigue así")
elif total >= 5:
    print("Has aprobado, pero puedes mejorar")