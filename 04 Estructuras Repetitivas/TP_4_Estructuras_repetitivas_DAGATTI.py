# Programación I
# Trabajo Práctico
# Unidad 4 - Estructuras repetitivas
# Dagatti, German Luis 
# 31.230.293

###__________________ PROBLEMA N° 1 _______________________
"""Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""
LIMITE_MIN = 0
LIMITE_MAX = 100
for i in range(LIMITE_MIN, LIMITE_MAX+1):
    print(i)


###__________________ PROBLEMA N° 2 _______________________
""" Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene."""
num =  int(input("Ingrese un numero entero: "))
largo = len(str(num))
print("")
print("________________________________________________________")
print("La cantidad de dígitos que tiene",num,"es :",largo)


###__________________ PROBLEMA N° 3 _______________________
"""Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores."""
num1 = int(input("ingrese el primer número entero: "))
num2 = int(input("ingrese el segundo número entero: "))
if num1<num2:
    num_min = num1
    num_max = num2
elif num1>num2:
    num_min = num2
    num_max = num1
else:
    print("ERROR!! Los números ingresados son iguales")
    exit()
suma=0
for i in range(num_min+1,num_max):
    suma=suma+i 
print("")
print("________________________________________________________")
print("La suma de todos los números enteros comprendidos entre",num_min,"y",num_max,"es",suma)

###__________________ PROBLEMA N° 4 _______________________
"""Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0."""
CORTE = 0
suma = 0
num = int(input("ingrese el primer número entero (0 para detener el programa): "))
if num == 0:
    print("Has ingresado un 0 como primer valor")
    print("Que tengas buenos días, ADIOS!!! ")
    exit()
while num !=CORTE:
    suma += num
    num = int(input("ingrese otro número entero (0 para detener el programa): "))
print("")
print("________________________________________________________")
print("El total acumulado es:",suma)

###__________________ PROBLEMA N° 5 _______________________
"""Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""
import random
incognita =random.randint(0,9)
print("Bienvenido a este espectacular juego. ADIVINE EL NÚMERO SECRETO ENTRE 0 Y 9")
num = int(input("Ingrese el número que elijió: "))
if incognita == num:
    print("Felicitaciones adivinastes el número secreto (",num,") en 1 intento")
    exit()

cont = 1
while num !=incognita:
    cont +=1
    print(" OH! OH!, El número seleccionado es incorrecto. Vamos de nuevo")
    num = int(input("ingrese otro número: "))
print("")
print("________________________________________________________")
print("Felicitaciones adivinastes el número secreto (",num,") en",cont,"intentos")

###__________________ PROBLEMA N° 6 _______________________
"""Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente."""
LIMITE_MIN = 0
LIMITE_MAX = 100
num = LIMITE_MAX
i = LIMITE_MIN
while LIMITE_MIN <=i<= LIMITE_MAX:
    print(num)
    num -=2
    i +=2

###__________________ PROBLEMA N° 7 _______________________
"""Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario"""
LIMITE_MIN = 0

num = int(input("Ingrese un número entero positivo cualquiera: "))
if num<0:
    print("El número ingresado no es válido; no se aceptan números negativos. ")
    exit()
else:
    i = LIMITE_MIN
    sum=0
    for i in range(LIMITE_MIN, num+1):
        sum+=i
print("")
print("________________________________________________________")
print("La suma total es",sum)

###__________________ PROBLEMA N° 8 _______________________
"""Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""
LIMITE_MAX = 100
par = impar = negativo = positivo = 0
for i in range(0, LIMITE_MAX):
    num = int(input("Ingrese un número entero cualquiera: "))
# Contamos los números positivos y negativos
    if num<0:
        negativo +=1
    else:
        positivo +=1
# Contamos los números pares e impares 
    if num%2==0:
        par+=1
    else:
        impar +=1
    i+=1
print("")
print("________________________________________________________")
print("LOS RESULTADOS SON")
print("La cantidad total de numeros positivos es",positivo)
print("La cantidad total de numeros negativos es",negativo)
print("La cantidad total de numeros pares es",par)
print("La cantidad total de numeros impares es",impar)


###__________________ PROBLEMA N° 9 _______________________
"""Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor)."""
LIMITE_MAX =100
suma = 0
for i in range(0, LIMITE_MAX):
    num = int(input("Ingrese un número entero cualquiera: "))
    suma += num
    i+=1
media = suma/LIMITE_MAX
print("")
print("___________________________________________")
print("La media de los numeros ingresados es",media)


###__________________ PROBLEMA N° 10 _______________________
"""Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

num = input("Ingrese un número entero cualquiera: ")
numero_invertido = num[::-1]  # Invierte el orden de los caracteres
print("___________________________________________")
print("El número invertido es:",numero_invertido)

# Resolución usando una estructura repetitiva
numero_invertido_2 = ""
indice = len(num) - 1
while indice >= 0:
    numero_invertido_2 += num[indice]
    indice -= 1
print("___________________________________________")
print("Ahora con While")
print("El número invertido es:",numero_invertido_2)