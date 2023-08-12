"""Ejercicio 1"""
n = 20
for num in range(2, n + 1):
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num)

"""Ejercicio 2"""
condimento = ''
while condimento != 'salir':
    condimento = input("Ingresa un condimento (o escribe 'salir' para terminar): ")
    if condimento != 'salir':
        print("Se ha agregado el condimento al sándwich.")

"""Ejercicio 3"""
tamaño = "S"
mensaje = "Hola, mundo!"
print("Tamaño de la remera:", tamaño)
print("Mensaje impreso:", mensaje)

"""Ejercicio 4"""
n = 10
fibo_sequence = [0, 1]
if n <= 2:
    print(fibo_sequence[:n])
while len(fibo_sequence) < n:
    next_num = fibo_sequence[-1] + fibo_sequence[-2]
    fibo_sequence.append(next_num)
print(fibo_sequence)

"""Ejercicio 5"""
x = float(input("Ingresa el primer número: "))
y = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa el número de la operación que deseas realizar (1: suma, 2: resta, 3: multiplicación, 4: división): ")
if operacion == '1':
    resultado = x + y
elif operacion == '2':
    resultado = x - y
elif operacion == '3':
    resultado = x * y
elif operacion == '4':
    resultado = x / y
else:
    resultado = "Operación no válida"
print("El resultado es:", resultado)

"""Ejercicio 6"""
gramos = 500
libras = gramos * 0.00220462
print(gramos, "gramos equivale a", libras, "libras")

centimetros = 100
pulgadas = centimetros * 0.393701
print(centimetros, "centímetros equivale a", pulgadas, "pulgadas")

kilometros = 5
millas = kilometros * 0.621371
print(kilometros, "kilómetros equivale a", millas, "millas")

libras = 10
gramos = libras / 0.00220462
print(libras, "libras equivale a", gramos, "gramos")

pulgadas = 20
centimetros = pulgadas / 0.393701
print(pulgadas, "pulgadas equivale a", centimetros, "centímetros")

millas = 3
kilometros = millas / 0.621371
print(millas, "millas equivale a", kilometros, "kilómetros")

"""Ejercicio 7"""
desde_año = 2000
año_actual = 2023
bisiestos = []
for año in range(desde_año, año_actual + 1):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        bisiestos.append(año)
print("Años bisiestos desde el año", desde_año, "hasta el año", año_actual, "son:", bisiestos)

"""Ejercicio 8"""
limite = 1000
suma = 0
for num in range(limite):
    if num % 3 == 0 or num % 5 == 0:
        suma += num
print("La suma de los múltiplos de 3 o 5 menores a", limite, "es:", suma)
