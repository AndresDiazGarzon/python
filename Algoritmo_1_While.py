"""
Definiciones básicas:
Es un ciclo repetitivo que esta condicionado
por una o varias variables. Permite detener
el ciclo cuando la condicion deje de cumplirse.

Su estructura básica es 
while(a>b){
}

Su estructura en python es
while a>b:
    ----

La pregunta de la condicion se da en cada iteracion.
"""

# Realiza un programa que permita contar desde 1 hasta x,
# siendo x ingresado por el usuario. Al contrario

print("Sistema de CONTEO")

x = int(input("¡Dame un número! - "))

i = 1

while i <= x:
    print(i)
    i += 1

print("__________Contrario___________")

j = x

while j > 0:
    print(j)
    j -= 1

print("__________De_2_en_2___________")

i = 1

while i <= x:
    print(i)
    i += 2

print("__________De_3_en_3___________")

i = 1

while i <= x:
    print(i)
    i += 3

print("Fin del sistema")
