# edad = int(input("Ingresa tu edad para saber si eres o no mayor de edad en polombia: "))
# if edad > 17:
#     print("En polombia eres mayor de edad con",edad, "años")
# else:
#     print("En polombia con",edad,"años eres mor de edad")

numero = int(input("Ingresa un número: "))
numero2 = int(input("Ingresa un nuevo número: "))
if numero > numero2:
    print(numero,"Es mayor a",numero2 )
elif numero == numero2:
    print(numero,"Es igual a",numero2)
else:
    print(numero,"Es menor a",numero2)