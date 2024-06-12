# Ejercicio 1
# Realice un algoritmo que permita capturar el nombre de un estudiante,
# sus calificaciones del 60% divididas en tres notas. El algoritmo
# debe mostrar al menos tres alternativas de notas para que pueda ganar 
# la materia con dos porcentajes del 20%. Se gana con 3.0

print("Bienvenidos al sistema PIERDE")

n=input("¿Desea calcular una nota? S/N: ")
Usuarios = []
CalUsu = []
while n == "S" or n == "s":
    Nombre = input("Dame tu nombre: ")
    Usuarios.append(Nombre)
    lis60 = []

    for i in range(3):
        nota = float(input(f"Ingresa la nota {i+1}: "))
        lis60.append(nota)
        if i == 2:
            CalUsu.append(lis60)


    # Calculos 
    nota60 = 0
    for nota in lis60:
        nota60 = nota60 + nota

    prom60 = (nota60 / 3)*0.6

    if prom60 == 1: 
        print("Tus notas deben ser de 5.0 para poder ganar")
    elif prom60 > 1 and prom60 <= 1.7:
        print("Todavia tienes esperanzas de ganar, pero con notas en el 40 porciento altas")
    elif prom60 > 1.7 and prom60 <= 2.9:
        print("Vas por buen camino, tus notas minimo deben ser de 3.0 en adelante")
    elif prom60 == 3:
        print("Amigo, ya ganaste el resto son ganas de más")
    else:
        print("Amigo, rindete... esto no lo tuyo")
    
    n = input("¿Desea calcular una nota? S/N: ")

print("La lista de los usuarios que utilizaron el sistema hoy fueron: ", Usuarios, " Las notas fueron ", CalUsu)
for est in range(len(Usuarios)):
    print(Usuarios[est])
    for i in range(len(CalUsu)):
        print(CalUsu[est][i])

print("Fin del sistema")