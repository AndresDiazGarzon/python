# Realice un algoritmo que permita capturar x cantidad de personas
# solicitando los datos de nombre, genero, edad y telefono. 
# El objetivo es poder conocer los siguientes datos:
# 1. Cantidad de mujeres mayores de edad
# 2. Cantidad de hombres menores de edad
# 3. Porcentaje de mujeres registradas
# 4. Porcentaje de hombres registrados
# 5. Promedio de edades de hombres y mujeres
# 6. Listado total de las personas registradas

print("Bienvenido al sistema")

CatPer = 0

CatPer= int(input("Ingrese la cantidad de personas: "))

Nalist = []
Genlist = []
Edadlist = []
Telist = []

for i in range(CatPer):
    nom = input(f"Ingresa tu nombre {i+1}: ")
    Nalist.append(nom)
    gen = input(f"Ingresa tu genero (F o M) {i+1}: ")
    Genlist.append(gen.upper())
    edad = int(input(f"Ingresa tu edad {i+1}: "))
    Edadlist.append(edad)
    cel = input(f"Ingresa el telefono {i+1}: ")
    Telist.append(cel)

total_Mujeres = total_Hombres = 0
cantHme = 0
cantMma = 0
cadena = ""
totEdades = 0

for i in range(CatPer): 
    cadena = cadena + str(Nalist[i]) + " - Teléfono: " + Telist[i] + "\n"
    totEdades += Edadlist[i]
    if Genlist[i] == "M":
        total_Hombres = total_Hombres + 1
        if Edadlist[i] < 18:
            cantHme += 1
    elif Genlist[i] == "F":
        total_Mujeres += 1
        if Edadlist[i] > 17:
            cantMma += 1

# 1. Cantidad de mujeres mayores de edad
print("__________________________________________")
print("Resultados de la encuesta")

print("La cantidad de mujeres mayores de edad es: ", cantMma)

# 2. Cantidad de hombres menores de edad
print("La cantidad de hombre menores de edad es: ", cantHme)

# 3. Porcentaje de mujeres registradas
porcentajeM = (total_Mujeres*100)/CatPer
print("El porcentaje de mujeres es: ", porcentajeM, "%" )

# 4. Porcentaje de hombres registrados
porcentajeH = (total_Hombres*100)/CatPer
print("El porcentaje de hombre es: ", porcentajeH, "%" )

# 5. Promedio de edades de hombres y mujeres
PromEdad = totEdades/CatPer
print("El promedio de edades es: ", PromEdad)

# 6. Listado total de las personas registradas
print("LISTADO TOTAL DE PERSONAS\n"+cadena)






