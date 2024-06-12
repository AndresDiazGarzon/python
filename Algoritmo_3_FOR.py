## Realiza un algoritmo donde el usuario ingrese un numero entero
## Definir desde el 1 hasta el numero cuales son pares y cuales impares
## Num % 2 == 0

# print("Bienvenidos al sistema numerico")

# x = int(input("Indiquenos un numero entero"))

# for vaca in range(x):
#     if (vaca+1) % 2 == 0:
#         print("El numero ", (vaca+1), " es par")
#     else:
#         print("El numero ", (vaca+1), " es impar")


## Realice un algoritmo que permita a un docente almacenar las 
## calificaciones de un grupo de x estudiantes. Debe imprimir
## Nombre del estudiantes, nota de programación, y al final un 
## promedio total de nota en el modulo

print("Bienvenido al sistema de NOTAS")

x = int(input("¿Profe, cuántos peludos son?"))

nombre = []
calificaciones = []

for i in range(x):
    nom = input("Nombre del estudiante ")
    nombre.append(nom)
    cal = float(input("Nota del estudiante "))
    calificaciones.append(cal)

promedio = suman = 0

for j in range(x):
    suman = suman + calificaciones[j]

promedio = suman/x

# Imprimimos los resultados
print("LISTADO DE ESTUDIANTES")
for h in range(x):
    print("Nombre: ", nombre[h], " tiene una nota de ", calificaciones[h])

print("PROMEDIO DEL GRUPO ES ", promedio)

print("Fin del programa")
