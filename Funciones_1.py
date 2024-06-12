# Las funciones son fragmento de codigo que se encargan
# de realizar una operacion especifica
# Su palabra reservada es def para declararla 
# Y llama a través de su nombre

# Definion de la funcion
# def Funcion_Suma():
#     print("Aqui se va a sumar")

# Para hacer un llamado (Call)
# Funcion_Suma()

## Realiza un algoritmo que me permita calcular las cuatro operaciones basicas
## de la matematicas a través de diferentes funciones

def operacionSuma(number1, number2):
    global suma 
    suma = number1 + number2
    print("El total de la suma de los dos valores es ",suma)

def operacionResta():
    resta = num1 - num2
    print("El total de la resta de los dos valores es ",resta)


def operacionDiv(n1,n2):
    global divi
    if n2 != 0:
        divi = n1 / n2
        print("El total de la división de los dos numeros es ", divi)
    else:
        print("Error, el cero no puede ser un valor para dividir")
        n2 = int(input("Ingrese de nuevo el segundo número"))
        # Recursividad: capacidad de llamarse a si mismo para repetir una operacion
        # Ayuda al ahorro del codigo, menos operaciones, menos carga para el sistema
        operacionDiv(n1, n2)


def operacionMulti(n1,n2):
    global multi
    if n1 != 0 and n2 != 0:
        multi = n1 * n2
        print("El total de la multiplicación de los dos numeros es ", multi)
    else:
        print("Error, el cero no puede ser un valor para multiplicar")
        n1 = int(input("Ingrese de nuevo el primer número"))
        n2 = int(input("Ingrese de nuevo el segundo número"))
        operacionMulti(n1, n2)


num1 = int(input("Dame un primer número: "))
num2 = int(input("Dame un segundo número: "))

operacionSuma(num1, num2)
operacionResta()
operacionDiv(num1, num2)
operacionMulti(num1, num2)
