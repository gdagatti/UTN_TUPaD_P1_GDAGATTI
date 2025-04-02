# Trabajo Práctico
# Unidad 1 - Estructuras secuenciales
# Dagatti, German Luis 
# 31230293

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo")


# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
#  Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.#
nombre = input("Ingrese su nombre: ")
print (f'"Hola {nombre}!"')


#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima 
# por pantalla una oración con los datos ingresados. Por ejemplo: 
# si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, 
# el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.#
nombre1 = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f'"Soy {nombre1} {apellido}, tengo {edad} años y vivo en {residencia}”.')


#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio = int(input("Ingrese el radio del círculo: "))
import math
area=math.pi*radio**2
perimetro = 2*math.pi*radio 
print(f"Dado un círculo de radio {radio}, tenemos que su area es: {area} y su perímetro es: {perimetro} ")


#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla 
# a cuántas horas equivale. #
segundos = int(input("Ingrese una cantidad de segundos "))
hora = segundos/3600
print(f"Los {segundos} segundos corresponden a {hora} horas")


#6) Crear un programa que pida al usuario un número e imprima por pantalla 
# la tabla de multiplicar de dicho número.
num1 = int(input("Ingrese un número cualquiera: "))
print(f"{num1} * 1 = {num1*1}\n{num1} * 2 = {num1*2}\n{num1} * 3 = {num1*3}\n{num1} * 4 = {num1*4}\n{num1} * 5 = {num1*5}\n{num1} * 6 = {num1*6}\n{num1} * 7 = {num1*7}\n{num1} * 8 = {num1*8}\n{num1} * 9 = {num1*9}\n{num1} * 10 = {num1*10}\n")


#7) Crear un programa que pida al usuario dos números enteros distintos del 0 
# y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 
num2 = int(input("Ingrese un número distinto de cero: "))
num3 = int(input("Ingrese otro número distinto de cero: "))
print(f"La suma de {num2} + {num3} es igual a {num3+num2}")
print(f"La resta de {num2} - {num3} es igual a {num3-num2}")
print(f"La multiplicación entre {num2} y {num3} es igual a {num3*num2}")
print(f"La división entre {num2} y {num3} es igual a {num2/num3}")


# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
#  Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:#
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
imc = peso/(altura**2)
print(f"El IMC para un peso de {peso} kilos y una altura de {altura} metros es de {imc}")


#9) Crear un programa que pida al usuario una temperatura en grados Celsius e 
# imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =95.𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
celsius = float(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit = 9/5*celsius + 32 
print(f"El equivalente de {celsius} grados Celsius es de {fahrenheit} grados Fahrenheit")


## 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
num4 = float(input("Ingrese un número cualquiera: "))
num5 = float(input("Ingrese otro número cualquiera: "))
num6 = float(input("Ingrese el último número cualquiera: "))
promedio = (num4+num5+num6)/3
print(f"El promedio de {num4}, {num5} y {num6} es igual a {promedio}")