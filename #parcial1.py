# Realice un algoritmo que me permita tener un control de los gastos mensuales. 
# El programa debe hacer lo siguiente:
# •	Solicite al usuario cual es el usuario y contraseña de ingreso 
# (tener como constante el nombre – Admin- y contraseña -123pormi-).
# •	Solicite al usuario el nombre de la persona y su salario mensual.
# •	Solicite al usuario que ingrese la cantidad de gastos que desea registrar en el mes (n).
# •	Solicite al usuario que ingrese los detalles de cada gasto, incluyendo una 
# breve descripción y el monto gastado.
# Al finalizar la entrada de datos, muestra un resumen que incluya:
# •	El total de gastos del mes.
# •	El total de gastos versus el total ganado.
# •	Un mensaje indicando si le queda dinero del salario o por el contrario le falta.

# •	El promedio de gastos por artículo.
# •	La descripción del gasto más caro max().
# •	La descripción del gasto más barato min().
# Además, podrías proporcionar una opción para que el usuario pueda buscar y 
# mostrar todos los gastos por encima o 
# por debajo de cierto umbral que él elija.



Contra = "123"
Usuario = "Admin"
lisAdmin=[]

def RegistroAdmin(usuario, contra):
    RegisAdmin = list((usuario, contra))
    lisAdmin.append(RegisAdmin)
    print("Registro exitoso!!")    
          
    
def ObtenerCredenciales():
    usu= input("ingresa el Usuario: ")
    pasword=input("Introduce la Contraseña: ")
    return usu, pasword    
    
    
def AccesoSistema():
    print("________________________________________________________________\n")
    print("____________Bienvenidos al sistema de Gastos Mensuales____________\n")
    
        
    x = int(input("Ingrese la cantidad de gastos Mensuales $: "))
    
    ## Lista de productos
    Nombre=[]
    salMensual = []
    mes=[]
    cantMensual=[]
    detDescripcion=[]
    detMonto=[]
    
    for i in range(x):
        nombre=input("\nIngrese su Nombre: ")
        Nombre.append(nombre)
        SalMensual=int(input("Ingrese su Salario Mensual $: "))
        salMensual.append(SalMensual)
        Mes=input("Ingrese Mes: ")
        mes.append(Mes)
        cantGastos = int(input(f"Ingrese la cantidad de gastos para el mes de {Mes} $: "))
        cantMensual.append(cantGastos)
        
        total_gastos = 0
        for j in range(cantGastos):
            descripcion = input(f"\nIngrese la descripción del gasto #{j + 1}: ")
            detDescripcion.append(descripcion)
            monto = int(input(f"Ingrese el monto del gasto #{j + 1}: "))
            detMonto.append(monto)  
            total_gastos += monto

        # Calcular el promedio de gastos
        promedio_gastos = total_gastos / cantGastos
            
        # Encontrar el gasto más caro
        monto_gasto_max = max(detMonto)
        index_gasto_max = detMonto.index(monto_gasto_max)
        descripcion_gasto_max = detDescripcion[index_gasto_max]

        # Encontrar el gasto más barato
        monto_gasto_min = min(detMonto)
        index_gasto_min = detMonto.index(monto_gasto_min)
        descripcion_gasto_min = detDescripcion[index_gasto_min]

        # Mostrar resumen
        print("________________________________________________________________\n")
        print("\nResumen de gastos mensuales:")
        print(f"Total de gastos del mes de {Mes}: ${total_gastos}")
        print(f"Total de gastos versus salario mensual: ${total_gastos - SalMensual}")
        if total_gastos > SalMensual:
            print("¡Te has excedido en tus gastos!")
        else:
            print(f"Todavía tienes ${SalMensual - total_gastos} disponible de tu salario.")

        print(f"Promedio de gastos por artículo: ${promedio_gastos:.2f}")
        print(f"Gasto más caro: {descripcion_gasto_max} - Monto: ${monto_gasto_max}")
        print(f"Gasto más barato: {descripcion_gasto_min} - Monto: ${monto_gasto_min}")
        print("________________________________________________________________\n")
            # Opción para buscar gastos por encima o por debajo de un umbral
    umbral = int(input("Ingrese un umbral para buscar gastos por encima o por debajo: "))
    print("\nGastos por encima del umbral:")
    for j in range(cantGastos):
            if detMonto[j] >= umbral:
                print(f"Descripción: {detDescripcion[j]}, Monto: ${detMonto[j]}")
    print("\nGastos por debajo del umbral:")
    for j in range(cantGastos):
            if detMonto[j] < umbral:
                print(f"Descripción: {detDescripcion[j]}, Monto: ${detMonto[j]}")    
        
    
    
def ValidarAdmin(usuario, contra):
    j = 0
    for i in range(len(lisAdmin)):
        valUsu = lisAdmin[i][0]
        if usuario == valUsu:
           ## print("El usuario existe")
            j = j + 1
            valCon = lisAdmin[i][1]
            if contra == valCon:
                ##print("La contraseña si es")
                ## Procesos nuevos de acceso al sistema
                AccesoSistema()
                return
            else:
                print("Usuario o Contraseña incorrectos.")
                print("La contraseña no es correcta")
                contra = input("Ingrese nuevamente la contraseña")
                ValidarAdmin(usuario, contra)
                

# #__________________________________________________________________________________________#
print("__________________________________________\n")
print("Bienvenidos al sistema de Gastos Mensuales")
Usu, pasword= ObtenerCredenciales()

while Usu!=Usuario or pasword != Contra:
    print("El Usuario o contraseña no es correcta. ")
    Usu, pasword= ObtenerCredenciales()

print("Usuario y Contraseña correcta.")

AccesoSistema()

    
