# Realiza un algoritmo que permita al usuario crear un registro de 3 personas
# solicitando sus datos personales como nombre, id, contraseña
# Cuando termine los registros, validar el ingreso al sistema... cuando ingrese
# mostrar un mensaje motivacionallll

# print("LOGIN-SYSTEM")

# print("REGISTRO de Administradores")

# i = 1
# Admin = []

# while i <= 3:
#     other = list((input("¡Ingresa el nombre!"), input("¡Ingresa el ID!"), input("¡Ingresa la contraseña!")))
#     Admin.append(other)
#     i += 1

# print("________VALIDAR_INGRESO__________")

# usuario = input("¡Ingresa tu ID!")
# contra = input("¡Ingresa tu Contraseña!")
# banderita = True
# i = 0

# while banderita:
#     if usuario == Admin[i][1]:
#         print("El usuario es correcto")
#         if contra == Admin[i][2]:
#             print("La contraseña es correcta")
#             print("BIENVENIDO AL SISTEMA")
#         else:
#             print("La contraseña NO es correcta")
#     else:
#         print("El usuario NO es correcto")
#     i += 1



# print(Admin)

usuario = "admin"
contra = "123pormi"

validaUsu = input("Ingrese el usuario: ")
validaCon = input("Ingrese la contraseña:")

while validaUsu != usuario and validaCon != contra:
    print("Error en los datos")
    validaUsu = input("Ingrese el usuario: ")
    validaCon = input("Ingrese la contraseña:")
else:
    print("Bienvenido al sistema")
    print("Lo invitamos a continuar en el proceso")
