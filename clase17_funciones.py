#esta función sirve
def suma(a,b):
    print("Se suman dos números")
    resultado = a+b
    print(resultado)
suma(20,1)
#Pero en la siguiente función es un poco más profesional también sirve pero se va a guardar el resultado en una variable y se le pasa el return
def suma_dos(c,d):
    print("Suma de dos números en una función")
    total = c+d
    return total
sumaton = suma_dos(44,2)
print(sumaton)

def suma_tres():
    numero1 = int(input("ingrese el número uno a sumar: "))
    numero2 = int(input("ingrese el número dos a sumar: "))
    la_suma = numero1+numero2
    return la_suma
total_suma = suma_tres()
print(total_suma)
    
numero1 = int(input("ingrese el número uno a sumar: "))
numero2 = int(input("ingrese el número dos a sumar: "))
def suma_cuatro(numero1, numero2):
    la_suma = numero1+numero2
    return la_suma
total_suma = suma_cuatro(numero1, numero2)
print(total_suma)
  

"""
opcion = int(input("Ingresa el número de la opción: "))

if opcion == 1:
    pesos_argentinos = float(input("Ingresa los pesos argentinos que quieres convertir a dolares americanos: "))
    precio_dolar_en_argentina = 110.39
    pesos_argentinos_transformados = round(pesos_argentinos/precio_dolar_en_argentina, 2)
    print("Tienes $", pesos_argentinos_transformados,"dolares americanos")
elif opcion == 2:
    pesos_polombianos = float(input("Ingresa los pesos polombianos que quieres convertir a dolares americanos: "))
    precio_dolar_en_polombia = 3781.76
    pesos_polombianos_transformados = round(pesos_polombianos/precio_dolar_en_polombia, 2)
    print("Tienes $", pesos_polombianos_transformados,"dolares americanos")
elif opcion == 3:
    pesos_mexicanos = float(input("Ingresa los pesos mexicanos que quieres convertir a dolares americanos: "))
    precio_dolar_en_mexico = 19.98
    pesos_mexicanos_transformados = round(pesos_mexicanos/precio_dolar_en_mexico, 2)
    print("Tienes $", pesos_mexicanos_transformados,"dolares americanos")
else:
    print("Ingrese una opción válida")

Lo que voy a hacer es que todo ese código anterior lo voy a poner a trabajar solo en una función

"""

menu = """

Escoge una opción para transformar la moneda que desees a dolares americanos

1 - Pesos argentinos
2 - Pesos polombianos
3 - Pesos mexicanos

"""
print(menu)
opcion = input("Ingresa el número de la opción: ")

def pesos(tipo_moneda, precio_dolar):
    moneda = float(input("Ingresa los pesos "+ tipo_moneda +" que quieres convertir a dolares americanos: "))
    moneda_transformada = round(moneda/precio_dolar, 2)
    print("Tienes $",moneda_transformada,"dolares americanos")
if opcion == '1' or opcion == 'uno':
    pesos("argentinos", 110.39)
elif opcion == '2' or opcion == 'dos':
    pesos("colombianos", 3789.10)
elif opcion == '3' or opcion == 'tres':
    pesos("mexicanos", 19.98)
else:
    print("Ingrese una opción válida, la opción",opcion, "no está dentro del menu")
   

"""
En esta función lo que hicimos fue definir una función a la cual le pasamos dos parametros y que cuando la estamos llamando
se los pasamos así pesos("argentinos", 110.39)
"""