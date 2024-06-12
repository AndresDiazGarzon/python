# print("Hello World")

# # Declaración de variables 
# a = 0
# b = 0.0
# c = "0"

# # COnocer el tipo de dato en python
# #type(variable)

# print(type(a))
# print(type(b))
# print(type(c))

# # Los tipos de datos para python con clases
# # Integer
# # Float
# # String

# d = True
#  # Booleanos son variables de dos estados True/False

# print(type(d))

# # Asignación multiple

# e, f, g = 5, 15, 4

# print(e)

# h, i, j = "Juan", "Mateo", 10

# print(h, i, j)

# # Igualaciones en cadena 
# num1 = num2 = num3 = 50

# print(num1)

# Listas son un conjunto de datos ordenado que pueden tener coherencia o no 
# entre ellos pero a una misma variable le puedo asignar varios valores.

# NomBre = ["Laura", "Juan Jose", "Andres"]

# print(NomBre)
# print(NomBre[0])

# nom1, nom2, nom3 = NomBre

# print(nom3)

# Tipos de datos
# Str, int, floatm complex
# list, tuple, range
# dict
# set, frozenset
# bool
# bytes
# bytearray
# memoryview

# Diferentes formas de impresion

# Si dos valores son de diferente tipo, entonces la coma (,) sera su concatenador
# Si dos valores son iguales tipo de dato, entonces el mas (+) sera su concatenador

# name = "Joel Yagari"
# age = 7

# print(name, age)

# name2 = "Joel"
# lasname = "Yagari"

# print(name2 + lasname)

# Conocer que son los def en python

# AnioActual = "2024"

# def myFunct():
#     print(AnioActual)

# myFunct()

# Variables globales que dentro del codigo se pueden acceder en cualquier momento
# Las variables locales solo se pueden acceder desde una función especifica

# Variable Global
# ciudad = "Madrid"

# def myCity():
#     # Variable local
#     ciudad = "Medellin"
#     print(ciudad)

# print(ciudad)
# myCity()

# Existen variables que puedo dentro del programa, sin importar si estan dentro
# de un def o no

# def myFruit():
#     global fruit
#     fruit = "Banano"

# myFruit()
# print(fruit)

# Las estructuras repetitivas me van a permitir generar procesos 
# multiples cuando utilice FOR o WHILE

# FOR
for i in range(10):
    print(i)