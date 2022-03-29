lista1 = ["hola", 1,"messi", 2, "mbappe", 3, "haaland", 4]
print(lista1)
#append -> para agregar un dato a una lista, podemos añadir, diccionarios, números, booleanos, etc.
agregar = lista1.append("Motos")
print(lista1)
#verificamos que tenemos motos en la lista
#pop -> para quitar un dato o eliminar de una lista le paso el indice de lo que quiero borrar y lo hace
lista2 = ["hola", 1,"messi", 2, "mbappe", 3, "haaland", 4]
print(lista2)
quitar = lista2.pop(5)
print("- aquí en esta lista ya no aparece el dato que estaba en el índice 5 que era el número 3",lista2)
lista_numeral = [98,76,90,33,100,100, 5,2,8,100,55,66]
print("- lista creada: ",lista_numeral)
lista_numeral.insert(4, 100)
print("- lista con el dato 100 insertado en la posición 4: ",lista_numeral)
lista_numeral.reverse()
print("- lista ordenada alreves: ",lista_numeral)
lista_numeral.sort()
print("- lista ordenada del más grande al más pequeño: ",lista_numeral)
indic = lista_numeral.index(33)
print("- la posición en la que está el número 33:",indic)
cuente = lista_numeral.count(100)
print("- las veces que está el 100 en la lista:",cuente)
lista_numeral.remove(5)
print("- lista sin el dato que le dije que elimine que es el 5, lista_numeral.remove(5)",lista_numeral)
del lista_numeral[4]
print("- lista sin el dato que le dije que elimine que es el que estaba en la posición 4, del lista_numeral[4]",lista_numeral)
lista_extender = [99, 98,97,96,95]
lista_numeral.extend(lista_extender)
print("- la primera lista extendida con estos datos: lista_extender = [99, 98,97,96,95], lista extendida:",lista_numeral)