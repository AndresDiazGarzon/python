# Realice un programa que enumere los paises de la siguiente lista:
# Canada, USA, Mexico y Australia. Y permita ingresar la cantidad de habitantes.
# Realice un promedio de los habitantes de estos.

# print("SISTEMA DE HABITANTES")

## Declaración de variables
# paises = ["Canada", "USA", "Mexico", "Australia"]
# habitantes = []
# sumHab =0

#Lectura de datos
# for i in range(4):
#     hab = int(input("¿Cuántos habitantes tiene " + paises[i] + "?: "))
#     habitantes.append(hab)

## Calcular el promedio de habitantes
# for j in range(4):
#     sumHab = sumHab + habitantes[j]

# promedio = sumHab/4

## Mostrar los resultados
# for n in range(4):
#     print("El pais ", paises[n], " tiene una cantidad de habitantes de ", habitantes[n])

# print("El promedio de habitantes de los cuatro paises es de ", promedio)

# print("Fin del sistema de paises")


## Generación de los numeros primos de n valores, donde n es un numero 
## entero positivo ingresado por el usuario.
## num % n != 0

## Escribir un programa que pregunte al usuario una cantidad a invertir, el interes
## anual y el numero de años, y muestre por pantalla el capital obtenido en la inversión
## cada año que dura la inversion

print("Bienvenido a la PIRAMIDE de MAY")

## Captura de los datos
CantInversion = float(input("¿Cuánto dinero desea invertir?"))
CantIntereses = float(input("¿Cuánto es la tasa de interes anual?"))
CantTiempo = int(input("¿Durante cuanto tiempo va invertir?\n* Indicar en años\n"))
Inversion = TotalInv = 0

## Procesar la información 
for i in range(CantTiempo):
    Inversion = CantInversion * (CantIntereses/100)
    TotalInv = TotalInv + Inversion
    CantInversion = CantInversion + Inversion

print("Capital final con interese\n", CantInversion, "\nIntereses obtenidos\n", TotalInv)

print("Fin del Piramide May")
