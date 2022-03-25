"""
las rebanadas consisten en acceder a las letras o indices de un string mediante rangos de letras

"""

string = input("ingresa un string para aplicarle una rebanada: " )
print("mi string es:",string)
print("con string[0], estoy obteniendo la letra que está en la posición cero de mi string:",string[0])
print("con string[:3], estoy obteniendo la letra que está en la posición cero de mi string hasta la posición 2:",string[0:3])
print("con string[4], estoy obteniendo la letra que está en la posición 4 de mi string:",string[4])
print("con string[3:7], estoy obteniendo las letras que están desde la posición 3 hasta la posición 6 de mi string:",string[3:7])
print("con string[3:], estoy obteniendo las letras que están desde la posición 3 hasta la posición final de mi string:",string[3:])
print("con string[::], estoy obteniendo todas las letras de mi string:",string[::])
print()
print("con string[1:8:2], estoy obteniendo la subcadena que están desde la posición 1 hasta la posición 8 de mi string pero en pasos de 2 en 2:",string[1:8:2])
print()
print("con string[1::3], estoy obteniendo la subcadena que están desde la posición 1 hasta la posición final de mi string pero en pasos de 3 en 3:",string[1::3])
print()
print("con string[::], estoy obteniendo todas las letras de mi string:",string[::])
print()
print("con string[::-1], estoy obteniendo todas las letras de mi string desde el principio hasta el final pero en pasos negativos:",string[::-1])
print("es decir voy desde el final hacía el principio, el string era:", string)