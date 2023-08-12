# """Ejercicio 1"""
# wasa=[]
# for numero in range (1,2000001):
#     wasa.append(numero)
# print(wasa)
# pepe=[]
# numeros=int(input("Ingrese hasta donde quiere ingresar numeros en una lista: "))
# for numero in range (0,numeros+1):
#     pepe.append(numero)
# """Ejercicio 2"""
# numeral=int(input("Ingrese el numero que quiere multiplicar hasta el 10: "))
# for numero in range(numeral,numeral*11,numeral):
#    print(numero)
"""Ejercicio 3"""
# string = input("Ingresa un string: ")
# letras = []
# for letra in string:
#     letras.append(letra)
# letras_unicas = list(set(letras))
# print("La lista de letras que no se repiten es:", letras_unicas)
"""Ejercicio 4"""
# cadena=input("Ingrese una frase: ")
# lista=[]
# for elemento in range(len(cadena)):
#     if cadena[elemento]!=" ":
#         lista.append(cadena[elemento])
"""Ejercicio 5"""
# tupla=(1,1,1,2,3,4,5,6,7,8,8,8,7,5,6)
# elpepe=int(input("Ingrese un numero: "))
# if elpepe==1:
#     print("El 1 se repite 3 veces")
# elif elpepe==2:
#     print("El 2 se repite 1 ves")
# elif elpepe==3:
#     print("El 3 se repite 1 ves")
# elif elpepe==4:
#     print("El 4 se repite 1 ves")
# elif elpepe==5:
#     print("El 5 se repite 2 veces")
# elif elpepe==6:
#     print("El 6 se repite 2 veces")
# elif elpepe==7:
#     print("El 7 se repite 2 veces")
# elif elpepe==8:
#     print("El 8 se repite 3 veces")
# else:
#     print("Ese numero no esta en la tupla")
#Me dio paja pensar otra forma porque tenia tareas xd
"""Ejercicio 6"""
# messi=(1,2,3,4,5,6,7,8,9,10,11,12)
# elpepe=int(input("Ingrese un numero del mes que quiere que se muestre (bastante inutil el programa): "))
# if elpepe==1:
#     print("Enero")
# elif elpepe==2:
#     print("Febrero")
# elif elpepe==3:
#     print("Marzo (El mes de mi cumple)")
# elif elpepe==4:
#     print("Abril")
# elif elpepe==5:
#     print("Mayo")
# elif elpepe==6:
#     print("Junio")
# elif elpepe==7:
#     print("Julio")
# elif elpepe==8:
#     print("Agosto")
# elif elpepe==9:
#     print("Septiembre")
# elif elpepe==10:
#     print("Octubre")
# elif elpepe==11:
#     print("Noviembre")
# elif elpepe==12:
#     print("Diciembre")
# else:
#     print("Ese numero no es un mes (totalmente un ERROR)")
"""Ejercicio 7"""
# tupla_numerosa_numeral_con_familia_numerosa_con_numeros=(1,2,3,4,5,-1,128321836127835612537124371253651246,1,1,1,1,12,3,3,4,23,411,24,124,21,321,4,1,31,23,124,12,312,4,324,1,12,1,412,4,42,132,41,12,142,31,312,3214,123,13,0)
# print(f"Esta es la tupla {tupla_numerosa_numeral_con_familia_numerosa_con_numeros}")
# print("El numero mayor es 128321836127835612537124371253651246 y el menor es -1 yay.")
"""Ejercicio 8""" 
diccionario={}
print("Ingrese 1 si quiere buscar un nombre")
print("Ingrese 2 si quiere agregar un nombre un nombre")
print("Ingrese 3 si quiere eliminar un nombre")
print("Ingrese 4 si quiere salir")
respuesta=input()
if respuesta==1:
    nombre_a_buscar=input("Ingrese el nombre: ")
    if nombre_a_buscar != diccionario[0:len]:
        print("Ese nombre no esta")
        breakpoint()