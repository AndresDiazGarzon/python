# ## Sistema de gestión de ventas para la tienda de DonPedro

# # Variables Globales: acceder a ellas desde cualquier método
# Id = ""
# Contra = ""
# Nombre = ""
# Apellido = ""
# Anio = 0
# Email = ""
# Movil = ""
# lisAdmin = []

# def RegistroAdmin(id, contra, nombre, apellidos, anio, email, movil):
#     RegisAdmin = list((id, contra, nombre, apellidos, anio, email, movil))
#     lisAdmin.append(RegisAdmin)
#     print("Registro exitoso!!")

# def AccesoSistema():
#     ## Lista de productos
#     listProd = ["Leche", "Arepas", "Huevos", "Salchichon"]
#     listPrec = [3400, 2500, 800, 2300]
#     listStock = [10, 10, 30, 8]

#     print("________BIENVENIDO A LA TIENDA DE PEDRO________")
#     print("Nuestra lista de productos y precios es la siguiente: ")
#     print(list(zip(listProd, listPrec, listStock)))
#     TotalVenta = 0

#     while input("Desea vender: S/N ").upper() == "S":
#         NombreCompra = input("Ingrese el nombre de la persona a facturar: ")
#         print(list(zip(listProd, listPrec, listStock)))
#         while input("Agregar productos a la compra: S/N").upper() == "S":
#             print("¡Ingresa el nombre del producto desea vender!")
#             prod = input()
#             m = 0
            
#             for productos in listProd:
#                 if productos == prod:
#                     precUnitario = listPrec[m]
#                     Stock = listStock[m]
#                     print("Cuántos productos requieres de ", productos)
#                     cant = int(input())
#                     if cant <= Stock:
#                         TotalVenta = TotalVenta + (precUnitario*cant)
#                         listStock[m] = Stock - cant
#                     else:
#                         print("Error! no tenemos suficientes productos para venderte")
#                         break
#                 m = m + 1
            
#             print("La compra va en $", TotalVenta)
#             print(list(zip(listProd, listPrec, listStock)))
#         print("_________FACTURACIÓN___________")
#         print("Nombre del cliente: ",NombreCompra)
#         print("Total de la compra es: $", TotalVenta, "COP")
#         print("¡¡Gracias por su compra!!")
#         print("_______FIN_FACTURACIÓN_________")
#         TotalVenta=0
#         cant = 0
#         Stock = 0

# def ValidarAdmin(id, contra):
#     j = 0
#     for i in range(len(lisAdmin)):
#         valID = lisAdmin[i][0]
#         if id == valID:
#            ## print("El usuario existe")
#             j = j + 1
#             valCon = lisAdmin[i][1]
#             if contra == valCon:
#                 ##print("La contraseña si es")
#                 ## Procesos nuevos de acceso al sistema
#                 AccesoSistema()
#             else:
#                 print("La contraseña no es correcta")
#                 contra = input("Ingrese nuevamente la contraseña")
#                 ValidarAdmin(valID, contra)
  
#     if j == 0:
#         print("El usuario no existe en el sistema")

# def MostrarRegistros():
#     print("__________MOSTRAR_REGISTRO_USUARIOS__________")
#     cadena = ""
#     for i in range(len(lisAdmin)):
#         cadena = cadena + "\nDNI: "+ str(lisAdmin[i][0])+"\nContraseña: "+ str(lisAdmin[i][1])+"\nNombre: "+ str(lisAdmin[i][2])+"\nApellidos: "+ str(lisAdmin[i][3])+"\nAño de Nacimiento: "+ str(lisAdmin[i][4])+"\nE-mail: "+ str(lisAdmin[i][5])+"\nMóvil: "+ str(lisAdmin[i][6])+"\n_______________________________\n"
#     print("Lista de usuario\n", cadena)

# def EliminarRegistros():
#     print("__________ELIMINAR_REGISTRO_USUARIOS__________")
#     MostrarRegistros()
#     valID = input("Ingrese el ID del usuario a eliminar: ")
#     bande = False
#     for i in range(len(lisAdmin)):
#         IDval = lisAdmin[i][0]
#         if valID == IDval:
#             lisAdmin.pop(i)
#             bande = True
#             print("Usuario eliminado con éxito")
#     if bande == False:
#         print("El usuario no existe en el sistema, intentelo de nuevo")
#     MostrarRegistros()

# def ModificarRegistros():
#     print("")

# def GestionAdmin():
#     print("")


# ## ______________________________________ ##
# ## Operaciones del Sistema

# print("Bienvenidos a la Tienda de Pedro")
# banderita = True

# while banderita:
#     print("____________________________________")
#     print("""Elija la opción deseada: 
#           1. Registrar usuario 
#           2. Mostrar registros actuales
#           3. Eliminar un registro 
#           4. Modificar un registro
#           5. Ingresar al Sistema 
#           6. Salir del sistema""")
#     opc = int(input())

#     if opc == 1:
#         ## Opciones para el caso 1
#         print("_______________________________________")
#         print("Sistema de Registro de Administradores")

#         Id = input("Cedula: ")
#         while Id == "":
#             print("Error! El campo no puede estar vacio")
#             Id = input("Cedula: ")
        
#         Contra = input("Contraseña: ")
#         while Contra == "":
#             print("Error! El campo no puede estar vacio")
#             Contra = input("Contraseña: ")
        
#         Nombre = input("Nombres: ")
#         while Nombre == "":
#             print("Error! El campo no puede estar vacio")
#             Nombre = input("Nombres: ")

#         Apellido = input("Apellidos: ")
#         while Apellido == "":
#             print("Error! El campo no puede estar vacio")
#             Apellido = input("Apellido: ")

#         Anio = int(input("Año de nacimiento: "))
#         while Anio == 0:
#             print("Error! El campo no puede estar vacio")
#             Anio = int(input("Año de nacimiento: "))
#         else:
#             while Anio < 1924 or Anio > 2009:
#                 print("Error! El rango de fechas es entre 1924 y 2009")
#                 Anio = int(input("Año de nacimiento: "))

#         Email = input("E-mail: ")
#         while Email == "":
#             print("Error! El campo no puede estar vacio")
#             Email = input("E-mail: ")

#         Movil = input("Móvil: ")
#         while Movil == "":
#             print("Error! El campo no puede estar vacio")
#             Movil = input("Móvil: ")

#         RegistroAdmin(Id, Contra, Nombre, Apellido, Anio, Email, Movil)

#     elif opc == 2: ## Mostrar los registros de los usuarios
#         MostrarRegistros()

#     elif opc == 3: ## Eliminar los registros de los usuarios
#         EliminarRegistros()
        
#     elif opc == 4: ## Modificar los registor de los usuarios
#         ModificarRegistros()

#     elif opc == 5:
#         ## Opciones para el caso 2
#         print("_________________________________")
#         print("Sistema de Ingreso")

#         Identificador = input("ID: ")
#         while Identificador == "":
#             print("Error! El campo no puede estar vacio")
#             Identificador = input("ID: ")

#         Contrasena = input("Contraseña: ")
#         while Contrasena == "":
#             print("Error! El campo no puede estar vacio")
#             Contrasena = input("Contraseña: ")
        
#         ValidarAdmin(Identificador, Contrasena)

#     elif opc == 6:
#         banderita = False
#     else:
#         ## Opciones error
#         print("Error!! Opción elegida no es correcta")

# print("Fin de la Tienda de Pedro")

#___________________________________________________________________
Contra = "123"
Usuario = "Admin"
lisAdmin = []

def RegistroAdmin(usuario, contra):
    RegisAdmin = (usuario, contra)
    lisAdmin.append(RegisAdmin)
    print("Registro exitoso!!")

def ObtenerCredenciales():
    usu = input("Ingresa el Usuario: ")
    pasword = input("Introduce la Contraseña: ")
    return usu, pasword

def AccesoSistema():
    print("__________________________________________\n")
    print("Bienvenidos al sistema de Gastos Mensuales")
    continuar = True

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
        

# Código principal
print("__________________________________________\n")
print("Bienvenidos al sistema de Gastos Mensuales")
Usu, pasword = ObtenerCredenciales()

while not ValidarAdmin(Usu, pasword):
    print("El Usuario o contraseña no es correcta. ")
    Usu, pasword = ObtenerCredenciales()

print("Usuario y Contraseña correcta.")
AccesoSistema()

while True:
    print("____________________________________")
    print("""Elija la opción deseada: 
          1. Acceder al sistema
          2. Buscar
          3. Modificar un registro
          4. Salir del sistema
          """)

    opc = int(input())

    if opc == 1:
        AccesoSistema()

    elif opc == 2:
        # Lógica para buscar
        # Implementa la lógica para buscar según tus necesidades
        pass

    elif opc == 3:
        # Lógica para modificar un registro
        # Implementa la lógica para modificar según tus necesidades
        pass

    elif opc == 4:
        print("Saliendo del sistema. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, elija una opción válida.")
