"""Punto 1"""
nombre=input("Hola usuario, ingrese su nombre: ")
numero=int(input(f"Hola, {nombre}, ingrese un numero del 1 al 30 y determinaremos si es par o inpar: "))
if numero==2 and 4 and 6 and 8 and 10 and 12 and 14 and 16 and 18 and 20 and 22 and 24 and 26 and 28 and 30:
  print(f"El numero {numero} es par")
elif numero>30:
   print("Dije del 1 al 30 noob")
else:
   print(f"El numero {numero} es inpar")
"""Punto 2"""
nombre=input("Hola usuario, ingrese su nombre: ")
edad=int(input(f"Hola {nombre} ingrese su edad e indicaremos en que etapa de la vida está: "))
if edad<2:
    print("Usted, señor mio, es un bebe, ni siquiera se porque pudo escribir su edad xd")
elif edad<4:
    print("Usted es un infante")
elif edad<12:
    print("Usted es un niño")
elif edad<20:
    print("Usted es un adolecente")
elif edad<65:
    print("Usted es un adulto")
else:
    print("Usted es un anciano")
"""Punto 3"""
while True:
    x=input("Escriba SI si quiere terminar el programa ")
    if x=="SI":
       break
"""Punto 4 y punto 5"""
x=1
while x!=101:
    print(x ,end=" ")
    x+=1
    if x==10:
        print("\n")
    if x==20:
        print("\n")
    if x==30:
       print("\n")
    if x==40:
        print("\n")
    if x==50:
        print("\n")
    if x==60:
        print("\n")
    if x==70:
        print("\n")
    if x==80:
        print("\n")
    if x==90:
        print("\n")
    if x==101:
        break