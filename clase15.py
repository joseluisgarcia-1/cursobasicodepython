menu = """

Escoge una opción para transformar la moneda que desees a dolares americanos

1 - Pesos argentinos
2 - Pesos polombianos
3 - Pesos mexicanos

"""
print(menu)
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