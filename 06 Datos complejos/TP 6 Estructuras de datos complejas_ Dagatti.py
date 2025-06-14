# Programación I
# Trabajo Práctico
# Unidad 6 - Estructuras de datos complejas
# Dagatti, German Luis 
# 31.230.293

###__________________ PROBLEMA N° 1 _______________________
"""Dado el diccionario precios_frutas 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 

Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300."""

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(f"Antes {precios_frutas}")
precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300
print(f"Después {precios_frutas}")


###__________________ PROBLEMA N° 2 _______________________
"""Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800."""

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300
print(f"Resultado Preblema 1 {precios_frutas}")

# Desarrollo Problema 2
precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melón"]=2800
print(f"Después {precios_frutas}")


###__________________ PROBLEMA N° 3 _______________________
"""Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado 
en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios."""

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300
print(f"Resultado Preblema 1 {precios_frutas}")

# Desarrollo Problema 2
precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melón"]=2800
print(f"Después {precios_frutas}")

# Desarrollo Problema 3
print(precios_frutas.keys())

###__________________ PROBLEMA N° 4 _______________________
"""Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe. Ejemplo:

contactos = {'German': 1145645645, 'Luis': 1157897897, 'Caren': 1161231231, 'Sara': 1132582582, 'Francisco':1123693693}
print(f"El contacto de Luis es {contactos["Luis"]}")"""

def cargar_contactos():
    """
    Función para cargar 5 contactos con su nombre como clave y número como valor.
    :return: Diccionario con los contactos.
    """
    contactos = {}
    print("Ingrese 5 contactos con su nombre y número de teléfono.")
    for i in range(5):
        nombre = input(f"Ingrese el nombre del contacto {i + 1}: ")
        numero = input(f"Ingrese el número de teléfono del contacto {i + 1}: ")
        contactos[nombre] = numero
    return contactos

def consultar_contacto(contactos):
    """
    Función para consultar el número de teléfono de un contacto.
    :param contactos: Diccionario con los contactos.
    """
    nombre = input("Ingrese el nombre del contacto que desea consultar: ")
    if nombre in contactos:
        print(f"El número de teléfono de {nombre} es: {contactos[nombre]}")
    else:
        print(f"No se encontró el contacto {nombre}.")

def main():
    # Cargar contactos
    contactos = cargar_contactos()
    
    # Consultar contacto
    consultar_contacto(contactos)

if __name__ == "__main__":
    main()


###__________________ PROBLEMA N° 5 _______________________
"""Solicita al usuario una frase e imprime: 
• Las palabras únicas (usando un set). 
• Un diccionario con la cantidad de veces que aparece cada palabra. 
Ejemplo:
Entrada --> Hola Mundo Hola 
Salida --> 
palabras_unicas: {'Hola', 'Mundo'}
recuentos: {'Hola': 2, 'Mundo': 1} 
"""

def analizar_frase():
    # Solicitar la frase al usuario
    frase = input("Ingrese una frase: ")
    
    # Separar la frase en palabras
    palabras = frase.split()
    
    # Crear un conjunto de palabras únicas
    palabras_unicas = set(palabras)
    
    # Crear un diccionario para contar la cantidad de veces que aparece cada palabra
    recuentos = {}
    for palabra in palabras:
        if palabra in recuentos:
            recuentos[palabra] += 1
        else:
            recuentos[palabra] = 1
    
    # Imprimir los resultados
    print(f"palabras_unicas: {palabras_unicas}")
    print(f"recuentos: {recuentos}")

# Ejecutar la función
if __name__ == "__main__":
    analizar_frase()

###__________________ PROBLEMA N° 6 _______________________
"""Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
Luego, mostrá el promedio de cada alumno. 
Ejemplo: 
alumnos ={
    "Sofia": (10,9,8),
    "Luis": (6,7,7)
}
"""
def calcular_promedio(notas):
    return sum(notas) / len(notas)


# Inicializar el diccionario de alumnos
alumnos = {}

# Solicitar datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    notas = input(f"Ingrese las 3 notas de {nombre} separadas por comas (ejemplo: 10,9,8): ")
    notas = tuple(map(int, notas.split(',')))  # Convertir la entrada en una tupla de enteros
    alumnos[nombre] = notas

# Calcular y mostrar el promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = calcular_promedio(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")



###__________________ PROBLEMA N° 7 _______________________
""" Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
y Parcial 2: 
• Mostrá los que aprobaron ambos parciales. 
• Mostrá los que aprobaron solo uno de los dos. 
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 
"""
# Conjuntos de estudiantes aprobados
parcial1 = {1, 2, 3, 4, 5} #Conjunto de estudiantes que aprobaron el Parcial 1
parcial2 = {4, 5, 6, 7, 8} #Conjunto de estudiantes que aprobaron el Parcial 2

# Estudiantes que aprobaron ambos parciales
ambos_aprobados = parcial1.intersection(parcial2)
print(f"Estudiantes que aprobaron ambos parciales: {ambos_aprobados}")

# Estudiantes que aprobaron solo uno de los dos parciales
solo_uno_aprobado = parcial1.symmetric_difference(parcial2)
print(f"Estudiantes que aprobaron solo uno de los dos parciales: {solo_uno_aprobado}")

# Lista total de estudiantes que aprobaron al menos un parcial
al_menos_uno_aprobado = parcial1.union(parcial2)
print(f"Lista total de estudiantes que aprobaron al menos un parcial: {al_menos_uno_aprobado}")


###__________________ PROBLEMA N° 8 _______________________
"""  Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
Permití al usuario: 
• Consultar el stock de un producto ingresado. 
• Agregar unidades al stock si el producto ya existe. 
• Agregar un nuevo producto si no existe. 
"""

# Inicializar el diccionario de productos y su stock
productos = {}

while True:
    print("\nOpciones:")
    print("1. Consultar el stock de un producto")
    print("2. Agregar unidades al stock de un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Salir")
    
    opcion = input("Ingrese el número de la opción que desea realizar: ")
    
    if opcion == '1':
        # Consultar el stock de un producto
        nombre_producto = input("Ingrese el nombre del producto que desea consultar: ")
        if nombre_producto in productos:
            print(f"El stock de {nombre_producto} es: {productos[nombre_producto]}")
        else:
            print(f"El producto {nombre_producto} no existe en el stock.")
    
    elif opcion == '2':
        # Agregar unidades al stock de un producto existente
        nombre_producto = input("Ingrese el nombre del producto al que desea agregar unidades: ")
        if nombre_producto in productos:
            cantidad = int(input("Ingrese la cantidad de unidades a agregar: "))
            productos[nombre_producto] += cantidad
            print(f"Se han agregado {cantidad} unidades a {nombre_producto}. Stock actual: {productos[nombre_producto]}")
        else:
            print(f"El producto {nombre_producto} no existe en el stock.")
    
    elif opcion == '3':
        # Agregar un nuevo producto
        nombre_producto = input("Ingrese el nombre del nuevo producto: ")
        if nombre_producto not in productos:
            cantidad = int(input("Ingrese la cantidad inicial de stock: "))
            productos[nombre_producto] = cantidad
            print(f"Producto {nombre_producto} agregado con éxito. Stock inicial: {productos[nombre_producto]}")
        else:
            print(f"El producto {nombre_producto} ya existe en el stock.")
    
    elif opcion == '4':
        # Salir del programa
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")


###__________________ PROBLEMA N° 9 _______________________
""" Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
Ejemplo:
agenda = {
    ("lunes", "10:00"): "Reunión,
    ("martes", "15:00"): "Clase de inglés"
    }
Permití consultar qué actividad hay en cierto día y hora. 
"""

def consultar_evento(agenda, dia, hora):
    evento = agenda.get((dia, hora))
    if evento:
        return f"El evento programado para el {dia} a las {hora} es: {evento}"
    else:
        return f"No hay evento programado para el {dia} a las {hora}."

# Crear la agenda
agenda = {
("lunes", "10:00"): "Reunión",
("martes", "15:00"): "Clase de inglés",
("miércoles", "11:00"): "Turno médico",
("jueves", "14:00"): "Entrenamiento",
("viernes", "16:00"): "Cena con amigos"}
    
# Consultar un evento
dia = input("Ingrese el día de la semana (lunes, martes, miércoles, etc.): ")
hora = input("Ingrese la hora (formato HH:MM): ")

# Mostrar el resultado
print(consultar_evento(agenda, dia, hora))


###__________________ PROBLEMA N° 10 _______________________
""" Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
diccionario donde: 
• Las capitales sean las claves. 
• Los países sean los valores. 
Ejemplo: 
original = {"Argentina" : "Buenos Aires", "Chile": "Santiago"}
invertido = {"Buenos Aires": "Argentina", "Santiago": "Chile"}
"""
# Diccionario de ejemplo
entrada = input('Ingrese los datos de a pares del tipo Pais : Capital. Ej:País_1: Capital, País_2: Capital_2, ...:\n')

# Convertir la entrada en pares clave-valor y armar el diccionario
pares = entrada.split(",")
original = {}
for par in pares:
    # Dividir cada par en clave y valor
    clave, valor = par.split(":")
    original[clave.strip()] = valor.strip()

#Invertir el diccionario
invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais

print(f"Diccionario original: {original}")
print(f"Diccionario invertido: {invertido}")

