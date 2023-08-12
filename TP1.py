"""TP 1"""
"""Ejercicio 1"""
Mensajesimple="hola como estas?"
print(Mensajesimple)
Mensajesimple="bien y tu?"
print(Mensajesimple)

"""Ejercicio 2"""
Nombre="Pepito,"
print(Nombre+" quieres venir a comer en a mi casa?")

"""Ejercicio 3"""
print(4+4)
print(9-1)
print(2*4)
print(16//2)

"""Ejercicio 4"""
mi_entero=int (2.5)
mi_decimal=float (2)
mi_string=str ("hola")
mi_booleano=bool ("adios")
print(type(mi_entero))
print(type(mi_decimal))
print(type(mi_string))
print(type(mi_booleano))

"""Ejercicio 5"""
omg=int (2.95354356)
print(omg)

"""Ejercicio 6"""
#1 != 2
#Salida:True
#True == 1
#Salida:True
#False != False
#Salida:False
#False > 0
#Salida:False
#1.0 < 1
#Salida:False
#“test” == “test”
#Salida:True
#1.0 >= 1
#Salida:False

"""Ejercicio 7"""
mensaje=input("Hola, ¿como te llamas?")
print(f"Hola {mensaje}, un gusto en conocerte, averiguaremos cuantos años te faltan para tener 100 años")
mensaje=input ("¿Cuantos años tienes?")
resultadofinal=(100-int(mensaje)) 
print(f"Te faltan {resultadofinal} para tener 100 años")

"""Ejercicio 8"""
mensaje=input(f"Este programa sirve para pasar grados celsius a fahrenheit, ingrese la cantidad de grados que quiere pasar")
resultado=(int(mensaje)*9/5+32)
print(f"Serian {resultado} en total")

"""Ejercicio 9"""
mensaje1=input(f"Este programa es una calculadora simple, por favor ingrese su primer numero para sumarlo, restarlo, multiplicarlo, dividirlo normalmente y enteramente y potenciarlos")
mensaje2=input(f"Ingrese su segundo numero porfavor")
print(int(mensaje1)+int(mensaje2))
print(int(mensaje1)-int(mensaje2))
print(int(mensaje1)/int(mensaje2))
print(int(mensaje1)*int(mensaje2))
print(int(mensaje1)//int(mensaje2))
print(int(mensaje1)**int(mensaje2))
print(f"El 1ro es suma el 2do es resta el 3ro division el 4to multiplicacion 5to division entera 6to potenciacion")