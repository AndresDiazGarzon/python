# DEFINICIÓN DE LAS LISTAS
# Las listas son colecciones de datos ordenados, que nos permiten
# ingresar desde uno hasta multiples datos. Las listas se conocen
# en programación como los arrays - arreglos de de un sistema 
# list, set, tuplas, diccionarios

# listEst = ["Tomas", "Santiago", "Juan Jose"]

# print(listEst)

# Las listas cuando tienen rangos se puede configurar sus tres valores
# inicio, final, incremento (0,10,1)
# Version abrebiada es (10)
# listEst = ["Tomas", "Santiago", "Juan Jose"]

#Forma 1
# for est in reversed(listEst):
#     print(est)

#Forma 2
# longitud = len(listEst)
# for i in range(longitud-1,-1,-1):
#     print(listEst[i])

#Forma 3
# for estudiantes in listEst[::-1]:
#     print(estudiantes)

#Forma 4
# print(listEst[::-1])

# Recorrido de las listas se puede hacer a través de sus valores
# for est in listEst:
#     print(est)

# Tipos de datos que se pueden almacenar en las listas son:
# Caracteres, numeros enteros, booleanos y numeros decimales

# listCalEs = ["Joel Yagari", 7, 22.5, True, [3.0,5.0, 4.2, 2.2]]
# print(listCalEs)

# print(listCalEs[4][2])

# print(listCalEs[0:4])

MarcasMotos = ["Yamaha", "Ducatti", "BMW", "Suzuki", "Royal Enfield", "Harley Davidson"]
# print(MarcasMotos)

# # Insertar datos en una posición
# MarcasMotos.insert(2,"Benelli")
# print(MarcasMotos)

# # Eliminar los datos de una posición especifica
# MarcasMotos.remove("Ducatti")
# print(MarcasMotos)

# # Eliminar por una posición en especifico
# MarcasMotos.pop(2)
# print(MarcasMotos)

# # Limpiar la lista completa del sistema
# MarcasMotos.clear()
# print(MarcasMotos)

# Eliminar una posición y eliminación total de la lista
# del MarcasMotos[2]
# print(MarcasMotos)
# del MarcasMotos
# print("Helo")

# Otra forma de crear las listas es a traves de su funcion
# se llama a la funcion y se le envian los datos de la lista
listaColores = list(("Morado", "Azul", "Negro", "Blanco"))
print(listaColores)

DatosEstudiantes = [list(("Santiago","Medellín", 15, 0)), list(("Valentin", "San Valentin", 12, 1000))]
print(DatosEstudiantes)

print(DatosEstudiantes[0][0])
print(DatosEstudiantes[1][0])
n = 0
for i in range(4):
    print(DatosEstudiantes[n][i])
    if i == 1:
        n = n+1
        i = 0
