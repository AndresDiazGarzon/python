# # 1. Realizar un algoritmo que defina un vector con 10 posiciones y permita 
# # ingresar 10 números enteros entre 1 y 50. Imprima los siguientes resultados: 
# # suma de todos los número y multiplicación de las posiciones pares.

# print("Bienvenidos al sistema de NUMEROS ENTEROS")

# vector=[]
# sum=0
# multiplicacion=0

# for i in range(10):
     
#     num=int(input("ingrese un numero entero entre 1 al 50 :"))
#     if 1<= num <=50:
#         vector.append(num)
#     else:
#         print("Numero incorecto")
        
#         break
            
   

# for i in range(10):
#     sum= sum+vector[i]

# multiplicacion = vector[0]*vector[2]*vector[4]*vector[6]*vector[8]

# print("La suma de los números es: ",sum)
# print("La multiplicacion de los números pares es : ", multiplicacion)


# #___________________________________________________________________________
# # 2. Crea un algoritmo que solicite un número de mes al usuario (osea entre 1 y 
# # 12), y con este número me indique el nombre del mes al que corresponde.
# print("Bienvenidos al sistema MESES")
# vector=[]

# mes=int(input("Por favor ingrese un numero del 1 al 12: "))
# if mes==1:
#         vector.append(mes)
#         print("El mes es Enero")
# elif mes ==2:
#     vector.append(mes)
#     print("El mes es Febrero")
# elif mes ==3:
#     vector.append(mes)
#     print("El mes es Marzo")
# elif mes ==4:
#     vector.append(mes)
#     print("El mes es Abril")
# elif mes ==5:
#     vector.append(mes)
#     print("El mes es Mayo")
# elif mes ==6:
#     vector.append(mes)
#     print("El mes es Junio")
# elif mes ==7:
#     vector.append(mes)
#     print("El mes es Julio")
# elif mes ==8:
#     vector.append(mes)
#     print("El mes es Agosto")
# elif mes ==9:
#     vector.append(mes)
#     print("El mes es Septiembre")
# elif mes ==10:
#     vector.append(mes)
#     print("El mes es Octubre")
# elif mes==11:
#     vector.append(mes)
#     print("El mes es Noviembre")
# elif mes==12:
#     vector.append(mes)
#     print("El mes es Diciembre")
# else:
#         print("Numero incorecto")      


#___________________________________________________________________________
#3. Una empresa de transporte, quiere guardar el nombre de los conductores, el 
#salario y los kilómetros que conducen cada día de la semana. Para ello, se 
#debe guardar la información correspondiente a los nombres del conductor en 
#un vector tipo cadena, el salario en otro tipo float y otro para almacenar los 
#kilometros de cada día de la semana en enteros. Debe mostrar la lista con 
#los nombres de conductores, salarios y que me muestre el promedio de los 
#kilómetros recorridos por todos los conductores.
print("Bienvenidos al SISTEMA DE TRANSPORTE")

x= int(input("Ingrese la cantidad de conductores: "))

name =[]
salario =[]
kmDia =[]

for i in range(x):
    nom= input("Nombre del conductor es: ")
    name.append(nom)
    sal= float(input("Su salario es: "))
    salario.append(sal)
    kilometroDay= int(input("Su recorrido en kilometros es: "))
    kmDia.append(kilometroDay)

promedio= suma =0

for j in range(x):
    suma= suma+kmDia[j]

promedio= suma/x

print("Nombre:\n ",name,"Salario:\n",salario,"Kilometros al dia:\n",kmDia)
print("el promedio de kilometros de los conductores al dia es: ",promedio)


#___________________________________________________________________________
# 4. Realiza un programa que introduzca el nombre y la edad de cada alumno. Al 
# finalizar se mostrará los siguientes datos: los estudiantes mayores de edad, 
# cuál es la edad promedio de ellos y cuantos estudiantes se registraron.
# #___________________________________________________________________________
# 5. Se quiere realizar un algoritmo que lea por teclado las 5 notas obtenidas por 
# un estudiantes (comprendidas entre 0 y 5). A continuación debe mostrar 
# todas las notas, la nota promedio del curso, la nota más alta que ha sacado 
# y la menor.
# #___________________________________________________________________________
# 6. Realizar un algoritmo que permita crear un vector con N posiciones y permita 
# almacer valores aleatorios desde el programa. Debe mostrar el vector inicial 
# y despues el vector ordenado de menor a mayor

# 7. Realice un algoritmo que declare tres vectores de tipo entero ‘vector1’, 
# ‘vector2’ y ‘vector3’, con cinco posiciones cada uno; pida valores para 
# ‘vector1’ y ‘vector2’ y llene el valor del ‘vector3’ con la suma de los otros dos 
# (vector3=vector1+vector2).
# #___________________________________________________________________________
# # 8. Crear un algoritmo que me permita crear un vector de n posiciones y
# # almanece el tipo de sexo que tiene cada usuario, y al final me indique cuantos 
# # hombres y cuantas mujeres se registraron.
# #___________________________________________________________________________
# # 9. Realice un algoritmo que le permita a un usuario hacer la conversión de una 
# # cifra en pesos a dolares o euros, según el valor de cada moneda del día.
# print ("Bienvenidos al sismtema de CONVERSION")
# Val_pesos=float(input("Ingrese el valor en pesos: "))
# dolar= 3911.29
# euros= 4214.88
# # mostrar opciones de conversion
# print("\nOpciones de conversion:")
# print("1.Dolares")
# print("2.Euros")

# eleccion=int(input("seleccione el número de la moneda a la que desea convertir: "))

# if eleccion==1:
#     moneda="Dolares"
#     Val_moneda= Val_pesos/dolar
# elif eleccion==2:
#     moneda="Euros"
#     Val_moneda=Val_pesos/euros
# else:("Opcion no valida. Por favor, seleccione una opcion valida. ")

# print(f"Valor de la moneda elegida: {Val_moneda}")



# #___________________________________________________________________________
# 10.Realice un algoritmo que permita cálcular el salario de un empleado obtenido 
# durante un mes, pidiendo el valor del salario mensual y la cantidad de días 
# trabajados. Debe calcular el salario a pagar teniendo en cuenta que el 
# empleado tiene una deducción del 4% por conceptos de salud, el 4% por 
# concepto de pensión y el 2% por concepto de caja de compensación

# vSaliario= int(input("Ingrese el valor del salario mensual: "))
# cantDias= int(input("Ingrese la cantidad de dias laborados: "))
# salud=4
# pension=4
# compensacion=2

# vDia=0

# vDia=vSaliario/30

# salBruto=0
# salTotal=0

# salTotal=vDia*cantDias
# vPension= salTotal*pension/100
# vSalud= salTotal*salud/100
# vCompensacion= salTotal*compensacion/100
# salBruto=salTotal-vPension-vSalud-vCompensacion

# print("Su salario es: ",salBruto)


