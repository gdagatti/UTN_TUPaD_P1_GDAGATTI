# Programación I
# # Trabajo Práctico
# Unidad 11 - Recursividad
# Dagatti, German Luis 
# 31.230.293

###__________________ PROBLEMA N° 1 _______________________
"""Crea una función recursiva que calcule el factorial de un número. 
Luego, utiliza esa función para calcular y mostrar en pantalla el factorial 
de todos los números enteros entre 1 y el número que indique el usuario"""

#Deficinicón función recursiva 
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)



#Programa principal
numero= int(input("ingrese un número entero positivo: "))
for i in range(1, numero+1):  
    fac =factorial(i)
    print(f"El factorial del número {i} es igual a {fac}")
    i+=1

###__________________ PROBLEMA N° 2 _______________________
"""Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
Posteriormente, muestra la serie completa hasta la posición que el usuario especifique."""

#Deficinicón función recursiva 
def fibonacci(pos):
    if pos==0:
        return 1
    elif pos==1:
        return 1
    else:
        return fibonacci(pos-1)+ fibonacci(pos-2)



#Programa principal
print("La serie de Fibonacci de un número N, calcula la suma entre los dos números") 
print("resultantes de aplicar la serie de fibonacci a los anteriores inmediatos (N-1) y (N-2)")
print("Donde N es un número natural")
print("Por definición, la serie para 0 y 1 es igual a 1" )
numero= int(input("Ingrese un número N para calcular la serie de Fibonacci: "))
for i in range(1, numero+1):  
    resultado =fibonacci(i)
    print(f"La serie de Fibonacci del número {i} es igual a {resultado}")
    i+=1


###__________________ PROBLEMA N° 3 _______________________
"""Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
utilizando la fórmula 𝑛^𝑚= 𝑛∗𝑛^(𝑚−1). 
Prueba esta función en un algoritmo general."""

#Deficinicón función recursiva 
def potencia(n,m):
    if n==m==0:
        return -1
    elif m==0:
        return 1
    else:
        return n*potencia(n,m-1)



#Programa principal
base= int(input("Ingrese la base de la potencia: "))
exponente= int(input("Ingrese el exponente de la potencia: "))
resultado = potencia(base,exponente)
if resultado ==-1:
    print("No está definido la potencia de 0 elevada a la 0")
else:
    print(f"La potencia de base {base} y exponente {exponente} es igual a {resultado}")


###__________________ PROBLEMA N° 4 _______________________
"""Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
y devuelva su representación en binario como una cadena de texto."""

# Definición de la función recursiva
def decimal_a_binario(num):
    if num==0:
        return "0"
    elif num==1:
        return "1"
    else:
        return decimal_a_binario(num // 2) + str(num % 2)


#Programa principal
numero = int(input("Ingrese un número decimal entero positivo: "))
print(f"El número {numero} en binario es: {decimal_a_binario(numero)}")


###__________________ PROBLEMA N° 5 _______________________
"""Implementá una función recursiva llamada es_palindromo(palabra) 
que reciba una cadena de texto sin espacios ni tildes, 
y devuelva True si es un palíndromo o False si no lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed()."""

# Definición de la función recursiva
def es_palindromo(palabra):
    if len(palabra) <= 1:# Caso base: si la palabra es vacía o tiene un solo caracter, es un palíndromo
        return True
    if palabra[0] != palabra[-1]: # Si el primer y último caracter son distintos, no es un palíndromo
        return False
    return es_palindromo(palabra[1:-1]) # Llamada recursiva con la subcadena sin el primer y último caracter


#Programa principal
print("Se define como palíndromo a una palabra o frase que se lee igual de izquierda a derecha")
print("que de derecha a izquierda, ignorando la puntuación y los espacios")
print("Ejemplos de palabras:\n * radar\n * seres")
print('ejemplo de frases:\n * "Anita lava la tina"\n * "Dábale arroz a la zorra el abad"')
print("")
print("A continuación, para saber si es un palíndromo.")
palabra = input("Ingrese una cadena de texto sin espacios ni tildes: ").lower()
resultado = es_palindromo(palabra)
if resultado:
    print(f'La cadena de caracteres "{palabra.lower()}" es un palíndromo')
else:
    print(f'La cadena de caracteres "{palabra. lower()}" no es un palíndromo')


###__________________ PROBLEMA N° 6 _______________________
"""Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo 
y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)"""

# Definición de la función recursiva
def suma_digitos(n):
    if n < 10: # Caso base: si n es menor que 10, devuelve n directamente (último dígito)
        return n
    return (n % 10) + suma_digitos(n // 10) # Suma el último dígito y llama recursivamente con el número reducido

#Programa principal
num = int(input("Ingrese un número entero positivo: "))
if num>0:
    resultado = suma_digitos(num)
    print(f'La suma de suma de todos sus dígitos del número {num} es {resultado}')
else:
    print("ERROR: El número ingresado no es correcto")

###__________________ PROBLEMA N° 7 _______________________
"""Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, 
en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo 
y devuelva el total de bloques que necesita para construir toda la pirámide.
Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1))"""

# Definición de la función recursiva
def contar_bloques(n):
    if n == 1: # Caso base: si n es igual que 1, devuelve n directamente. 
        return 1
    else:
        return n + contar_bloques(n-1) # Suma el último dígito y llama recursivamente con el número reducido en 1

#Programa principal
num = int(input("Ingrese la cantidad de bloques en la base de la piramide: "))
if num>0:
    resultado = contar_bloques(num)
    print(f'Para crear una pirámide con {num} bloques como base, se necesitan un total de {resultado} bloques')
else:
    print("ERROR: La cantidad de bloques ingresada no es correcta")

###__________________ PROBLEMA N° 8 _______________________
"""Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo 
(numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4
contar_digito(123456, 7) → 0 """

# Definición de la función recursiva
def contar_digito(numero, digito):
    if numero == 0: # Caso base: si el número es 0, termina la recursión
        return 0
    # Si el último dígito es igual al buscado, suma 1 a la cuenta
    else: 
        if numero % 10 == digito:
            sum = 1 + contar_digito(numero // 10, digito)
        else:
            sum = 0 + contar_digito(numero // 10, digito)
    return sum

#Programa principal
num = int(input("Ingrese un número entero positivo : "))
dig = int(input("Ingrese un dígito entre 0 y 9: "))
if num>0:
    resultado = contar_digito(num,dig)
    print(f'Las veces que aparece el dígito {dig} dentro del número {num} es igual a {resultado}')
else:
    print("ERROR: La cantidad de bloques ingresada no es correcta")