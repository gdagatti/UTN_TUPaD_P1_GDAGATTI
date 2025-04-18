# Trabajo Práctico
# Unidad 3 - Condicionales
# Dagatti, German Luis 
# 31230293

###__________________ PROBLEMA N° 1 _______________________
"""Escribir un programa que solicite la edad del usuario. 
Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
"""
#Establecer la constante
EDAD_MAYOR = 18

# Solicitar información al usuario
edad_1 = int(input("Ingrese su edad: "))

# Mostrar resultado por pantalla
if edad_1 > EDAD_MAYOR:
    print("Es mayor de edad")

###__________________ PROBLEMA N° 2 _______________________
"""Escribir un programa que solicite su nota al usuario. 
Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
en caso contrario deberá mostrar el mensaje “Desaprobado”."""
#Establecer la constante
NOTA_MINIMA = 6

# Solicitar información al usuario
nota = int(input("Ingrese la nota obtenida: "))

# Mostrar resultado por pantalla
if nota >= NOTA_MINIMA :
    print("Aprobado")
else :
    print("Desaprobado")

###__________________ PROBLEMA N° 3 _______________________
"""Escribir un programa que permita ingresar solo números pares. 
Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; 
en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.."""

# Solicitar información al usuario
num = int(input("Ingrese un número par: "))

# Mostrar resultado por pantalla
if num%2 ==0 :
    print("Ha ingresado un número par")
else :
    print("Por favor, ingrese un número par")


###__________________ PROBLEMA N° 4 _______________________
"""Escribir un programa que solicite al usuario su edad e imprima por pantalla 
a cuál de las siguientes categorías pertenece: 
● Niño/a: menor de 12 años. 
● Adolescente: mayor o igual que 12 años y menor que 18 años. 
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años."""

# Solicitar información al usuario
edad = int(input("Ingrese su edad en años: "))

# Mostrar resultado por pantalla
if edad>=0 and edad<12 :
    print("Niño/a: menor de 12 años.")
elif edad>=12 and edad<18:
    print("Adolescente: mayor o igual que 12 años y menor que 18 años.")
elif edad>=18 and edad<30:
    print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años.")
elif edad>=30:
    print("Adulto/a: mayor o igual que 30 años.")
else:
    print("La edad ingresada es incorrecta")


###__________________ PROBLEMA N° 5 _______________________
"""Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje 
"Ha ingresado una contraseña correcta"; en caso contrario, 
imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
Nota: investigue el uso de la función len() en Python para evaluar 
la cantidad de elementos que tiene un iterable tal como una lista o un string."""
#Se establecen las constantes
LARGO_MINIMO = 8
LARGO_MAXIMO = 14

# Solicitar información al usuario
password = input("Ingrese una contraseña, debe tener entre 8 y 14 caracteres: ")

# Pido el largo de la contraseña
largo_password = len(password)  

#Mostrar mensaje de confirmación o error
if largo_password>=LARGO_MINIMO and largo_password<=LARGO_MAXIMO : 
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


###__________________ PROBLEMA N° 6 _______________________
"""El paquete statistics de python contiene funciones que permiten tomar una lista de números 
y calcular la moda, la mediana y la media de dichos números. 
Un ejemplo de su uso es el siguiente: 
    from statistics import mode, median, mean 
    mi_lista = [1,2,5,5,3] 
    mean(mi_lista) 
En la documentación oficial se puede encontrar más información sobre este paquete: 
https://docs.python.org/es/3.8/library/statistics.html. 
La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos 
que se pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, 
la mediana es mayor que la moda. 
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
la mediana es menor que la moda. 
● Sin sesgo: cuando la media, la mediana y la moda son iguales.
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, 
calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, 
negativo o no hay sesgo. 
Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma: 
    import random 
    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria."""
#Importar las librerias necesarias 
from statistics import mode, median, mean
import random 

#generar los números aleatorios 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#Cálculo de los stadísticos necesarios 
media = mean(numeros_aleatorios) 
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)

# Imprimir resultados en pantalla
if media > mediana and mediana > moda:
    print("La distribución normal tiene sesgo positivo")
elif media< mediana and mediana < moda:
    print("La distribución normal tiene sesgo negativo")
elif media == mediana == moda :
    print("La distribución normal no tiene sesgo")
else:
    print("No es una distribución normal")


###__________________ PROBLEMA N° 7 _______________________
"""Escribir un programa que solicite una frase o palabra al usuario. 
Si el string ingresado termina con vocal, añadir un signo de exclamación al final 
e imprimir el string resultante por pantalla; 
en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla."""

# Solicitar información al usuario
frase = input("Ingrese una frase o palabra cualquiera: ")
frase_low = frase.lower() # Ponemos el string en minúsculas 
ultima_letra = frase_low[-1] # seleccionamos la última letra del string

#Reescribir el string según corresponda
if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(f"{frase}!")
else:
    print(f"{frase}")


###__________________ PROBLEMA N° 8 _______________________
"""Escribir un programa que solicite al usuario que ingrese su nombre 
y el número 1, 2 o 3 dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario 
e imprimir el resultado por pantalla. 
Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas 
y minúsculas."""

# Solicitar información al usuario
nombre = input("Ingrese su nombre: ")
print("Escoja una de las opciones que se listan a continuación")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
opcion = int(input("Ingrese la opción seleccionada: "))

#Mostrar el nombre según la opción elegida por el ususrio
if opcion == 1:
    nombre_mayus = nombre.upper()
    print(f"{nombre_mayus}")
elif opcion == 2:
    nombre_minus = nombre.lower()
    print(f"{nombre_minus}")
elif opcion == 3:
    nombre_title = nombre.title()
    print(f"{nombre_title}")
else:
    print(f"La opción ingresada es incorrecta")


###__________________ PROBLEMA N° 9_______________________
"""Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de
las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)."""

# Solicitar información al usuario
escala = float(input("Ingrese la magnitud de un terremoto según la escala de Richter: "))

# Determinar la magnitud conforme a la escala de Richter
if escala <3:
    print(f'"Muy leve" (imperceptible)')
elif escala >=3 and escala < 4:
    print(f'"Leve" (ligeramente perceptible)')
elif escala >=4 and escala < 5:
    print(f'"Moderado" (sentido por personas, pero generalmente no causa daños)')
elif escala >=5 and escala < 6:
    print(f'"Fuerte" (puede causar daños en estructuras débiles)')
elif escala >=6 and escala < 7:
    print(f'"Muy Fuerte" (puede causar daños significativos)')
elif escala >=7:
    print(f'"Extremo" (puede causar graves daños a gran escala)')
else:
    print(f"La opción ingresada es incorrecta")


###__________________ PROBLEMA N° 10 _______________________
"""Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 

|Periodo del año                        |Estación en el hemisferio norte    |Estación en el hemisferio sur  |
|:-------------------------------------:|:---------------------------------:|:-----------------------------:|
|Desde el 21 de diciembre hasta el 20 de|Invierno                           |Verano                         |
|marzo (incluidos)                      |                                   |                               |
|Desde el 21 de marzo hasta el 20 de    |Primavera                          |Otoño                          | 
|junio (incluidos)                      |                                   |                               |
|Desde el 21 de junio hasta el 20 de    |Verano                             |Invierno                       |
|septiembre (incluidos)                 |                                   |                               |
|Desde el 21 de septiembre hasta el 20  |Otoño                              |Primavera                      | 
|de diciembre (incluidos)               |                                   |                               |

Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué
día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en
otoño, invierno, primavera o verano."""

# Solicitar información al usuario
hemisferio =input("Ingrese en que hemisferio se encuentra [S para sur, N para norte]: ").upper().strip()
mes = int(input("ingrese el mes del año en número (1 - 12). Ej: Enero es 1: "))
dia = int(input("Ingrese el día de hoy en números (1-31). Ej: Para lunes 10 solo ingrese 10: "))

# Determinar la estación según el hemisferio y la fecha
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

# Imprimir la estación correspondiente
print(f"Te encuentras en la estación: {estacion}")

