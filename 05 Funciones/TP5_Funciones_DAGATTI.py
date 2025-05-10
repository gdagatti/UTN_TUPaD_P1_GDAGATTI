# Programación I
# # Trabajo Práctico
# Unidad 5 - Funciones
# Dagatti, German Luis 
# 31.230.293

###__________________ PROBLEMA N° 1 _______________________
"""Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""

#Definicion de funciones 
def imprimir_hola_mundo():
    return print("Hola Mundo!")

#Programa principal
imprimir_hola_mundo()

###__________________ PROBLEMA N° 2 _______________________
"""Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
volver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""

#Definicion de funciones 
def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

#Programa principal
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

###__________________ PROBLEMA N° 3 _______________________
"""Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
dir los datos al usuario y llamar a esta función con los valores in-
gresados."""

#Definicion de funciones 
def informacion_personal(nombre, apellido,edad, residencia):
    return print(f"“Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}”")

#Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido,edad, residencia)

###__________________ PROBLEMA N° 4 _______________________
"""Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
dio como parámetro y devuelva el área del círculo. calcular_peri-
metro_circulo(radio) que reciba el radio como parámetro y devuel-
va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
bas funciones para mostrar los resultados"""
import math
#Definicion de funciones 
def calcular_area_circulo(radio):
    return print(f"El área de un círculo de radio {radio}, es igual {math.pi*(radio**2)}")

def calcular_perimetro_circulo(radio):
    return print(f"El perímetro de un círculo de radio {radio}, es de {math.pi*radio*2}")

#Programa principal
radio = float(input("ingrese el radio del círculo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

###__________________ PROBLEMA N° 5 _______________________
"""Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mos-
trar el resultado usando esta función."""

#Definicion de funciones 
def segundos_a_horas(segundos):
    horas=round(segundos/3600,2)
    hora=segundos//3600
    minuto = (segundos-hora*3600)//60
    segundo = segundos -(hora*3600+minuto*60)

    return print(f"Los {segundos} segundos corresponden a {horas} horas o lo que es lo mismo {hora} horas {minuto} minutos y {segundo} segundos")

#Programa principal
segundos = int(input("Ingresar los segundos que quiere pasar a horas: "))
print("_______________________________________________________________________")
segundos_a_horas(segundos)

###__________________ PROBLEMA N° 6 _______________________
"""Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función"""

#Definicion de funciones 
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


#Programa principal
num = int(input("Ingrese el número a multiplicar: "))
tabla_multiplicar(num)


###__________________ PROBLEMA N° 7 _______________________
"""Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resulta-
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara"""

#Definicion de funciones 
def operaciones_basicas(a, b):
    # Realizamos las operaciones básicas
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b 
    else:
        division ="ERROR!! No se puede dividir entre cero"
    
    # Retornamos los resultados como una tupla
    return suma, resta, multiplicacion, division


#Programa principal
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(a, b)

# Mostramos los resultados de forma clara
print(f"Resultados de las operaciones con {a} y {b}:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")


###__________________ PROBLEMA N° 8 _______________________
"""Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función 
para mostrar el resultado con dos decimales"""

#Definicion de funciones 
def calcular_imc(peso, altura):
    return print(f"Para un peso de {peso} kg y una altura de {altura} m, su IMC es igual a {round(peso/altura**2,2)}")

#Programa principal
peso = float(input("Ingrese su peso en Kg: "))
altura = float(input("Ingrese su altura en metros: "))
calcular_imc(peso, altura)

###__________________ PROBLEMA N° 9 _______________________
"""Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función."""

#Definicion de funciones 
def celsius_a_fahrenheit(celsius):
    return 9/5*celsius + 32


#Programa principal
celsius = float(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"El equivalente de {celsius} grados Celsius es de {fahrenheit} grados Fahrenheit")


###__________________ PROBLEMA N° 10 _______________________
"""Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función"""

#Definicion de funciones 
def calcular_promedio(a, b, c):
    return round((a+b+c)/3,2)


#Programa principal
num1 = float(input("Ingrese un número cualquiera: "))
num2 = float(input("Ingrese otro número cualquiera: "))
num3 = float(input("Ingrese el último número cualquiera: "))
print(f"El promedio de {num1}, {num2} y {num3} es igual a {calcular_promedio(num1,num2,num3)}")
