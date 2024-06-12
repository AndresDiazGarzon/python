# Realiza un algoritmo para un super mercado que permita
# registrar una cantidad de producto hasta que el usuario
# decida detenerse con un caracter. Mostrar total de los
# producto, el IVA y el total a pagar.

print("Bienvenidos al SuperMercado EL SABOR")

name = input("¿Cuál es tu nombre?: ")
dni = input("¿Cuál es tu DNI?: ")

listNameP = []
listCosteP = []
listCantP = []
NameP = "-"
CosteP = 0.0
CantP = 0
TotalProd = 0
IvaP = 0
TotalPago = 0

NameP = input("Ingrese el nombre del producto: ")

while NameP != "*":
    
    CosteP = float(input("Ingrese el costo del producto: "))
    CantP = int(input("¿Cuántos productos llevas?: "))

    listNameP.append(NameP)
    listCosteP.append(CosteP)
    listCantP.append(CantP)

    NameP = input("Ingrese el nombre del producto: ")

i = 0
# Operaciones de calculo
for Coste in listCosteP:
    TotalProd = TotalProd + (Coste*listCantP[i])
    i = i + 1

IvaP = TotalProd * 0.19
TotalPago = TotalProd + IvaP

# Imprimir los resultados
print(f"Señor@ {name} identificado con DNI {dni},\n su facturación es la siguiente:")
print(f"El total de los productos por la cantidad es ${TotalProd}COP")
print(f"El total del IVA es ${IvaP}COP")
print(f"El total a pagar es ${TotalPago}COP")
print("Gracias por usar nuestro sistema!!")
