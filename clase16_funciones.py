#funciones 
#llamando e imprimiendo una función 
# def imprimir_mensaje():
#     print("Hola amiguitos")
#     print("Espero que se encuentren bien")
#     print("Python es muy lindo")
#     print("Voy de camino en volverme un pythonista de alto nivel")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

"""Colocando parametros en la función y además llamándola"""


def saludo(mensaje):
    print("Hola amiguitos")
    print("Espero que se encuentren bien")
    print(mensaje)
    print("Voy de camino en volverme un pythonista de alto nivel")

opcion = int(input("Ingresa una opción 1, 2, 3: "))
if opcion == 1:
    saludo("Python es muy lindo, estás en la opción 1")
elif opcion == 2:
    saludo("Python es muy lindo, estás en la opción 2")
elif opcion == 3:
    saludo("Python es muy lindo, estás en la opción 3")
else:
    print("Escribe una opción correcta")

"""Con las funciones evitamos estar escribiendo tanto código repetido"""


