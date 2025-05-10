# Programación I
# # Trabajo Práctico
# Unidad 5.1 - Listas
# Dagatti, German Luis 
# 31.230.293

###__________________ PROBLEMA N° 1 _______________________
"""Crear una lista con los números del 1 al 100 que sean múltiplos de 4. 
Utilizar la función range.Crear una lista con los números del 1 al 100 
que sean múltiplos de 4. Utilizar la función range."""

lista_1 = list(range(4, 101, 4))
print(lista_1)

###__________________ PROBLEMA N° 2 _______________________
"""Crear una lista con cinco elementos (colocar los elementos que más te gusten) 
y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o 
bien investigar cómo funciona el indexing con números negativos!"""

lista_2 = list(range(0, 5))
print(lista_2)
print(lista_2[3]) # Indexing con números positivos 
print(lista_2[-2]) # Indexing con números negativos


###__________________ PROBLEMA N° 3 _______________________
"""Crear una lista vacía, agregar tres palabras con append e imprimir la lista 
resultante por pantalla. Pista: para crear una lista vacía debes colocar 
los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []"""

# Crear lista vacía
lista_3 = []
# Agregar los tres elementos con append
lista_3.append(3.5)
lista_3.append("hola")
lista_3.append(True)
# Imprir lista
print(lista_3)


###__________________ PROBLEMA N° 4 _______________________
"""Reemplazar el segundo y último valor de la lista “animales” con las palabras 
“loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. 
¡Puedes hacerlo como se muestra en los videos o bien investigar cómo 
funciona el indexing con números negativos! 
animales = ["perro", "gato", "conejo", "pez"]"""

# Crear lista 
animales = ["perro", "gato", "conejo", "pez"]
print("Lista original")
print(animales)
# Reemplazar valores
animales[1] = "loro"
animales[-1] = "oso" #indexing con números negativos
# Imprir lista
print("Lista modificada")
print(animales)


###__________________ PROBLEMA N° 5 _______________________
"""Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza
numeros =[8, 15, 3, 22,,7]
numeros.remove(max(numeros))
print(numeros)
"""

numeros = [8, 15, 3, 22, 7] # Crea la lista numeros 
numeros.remove(max(numeros)) # Remueve el valor mayor que está en numeros
print(numeros) # Imprime la lista numeros 


###__________________ PROBLEMA N° 6 _______________________
"""Crear una lista con números del 10 al 30 (incluído), 
haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
"""

# Crear la lista con range()
lista_6 = list(range(10, 31, 5))

# Mostrar los dos primeros elementos
print(lista_6[:2])


###__________________ PROBLEMA N° 7 _______________________
"""Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” 
por dos nuevos valores cualesquiera. 
autos = ["sedan", "polo", "suran", "gol"]
"""

# Crear la lista
autos = ["sedan", "polo", "suran", "gol"]

# Modificar los valores centrales 
autos[1] = "taos"
autos[2] = "nivus"

# Mostrar lista modificada
print(autos)


###__________________ PROBLEMA N° 8 _______________________
"""Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 
usando append directamente. 
Imprimir la lista resultante por pantalla.
"""

# Crear una lista vacía
dobles = []

# Agregar el doble de 5, 10 y 15
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

# Imprimir la lista resultante
print(dobles)


###__________________ PROBLEMA N° 9 _______________________
"""Dada la lista “compras”, cuyos elementos representan los productos comprados 
por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    a) Agregar "jugo" a la lista del tercer cliente usando append.
    b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
    c) Eliminar "pan" de la lista del primer cliente.
    d) Imprimir la lista resultante por pantalla
"""

# Crear la lista de compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente usando append
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")

# d) Imprimir la lista resultante por pantalla
print(compras)


###__________________ PROBLEMA N° 10 _______________________
"""Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes 
elementos:
    ● Posición lista_anidada[0]: 15
    ● Posición lista_anidada[1]: True
    ● Posición lista_anidada[2][0]: 25.5
    ● Posición lista_anidada[2][1]: 57.9
    ● Posición lista_anidada[2][2]: 30.6
    ● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla.
"""

# Crear la lista anidada con los valores indicados
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

# Imprimir la lista resultante
print(lista_anidada)