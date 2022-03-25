nombre = input("Ingresa tu nombre: ")
#coloca el string en mayúsculas
print("coloca el string en mayúsculas:",nombre.upper())
#coloca el string la primera letra en mayúscula
print("coloca el string la primera letra en mayúscula:",nombre.capitalize())
#si por ejemplo escribo un string y al final le pongo un espacio, ese se lo quito con strip()
print("quita los espacios que tiene al final el string:",nombre.strip())
#lower convierte el string todo en minúsculas
print("coloca el string todo en minúsculas:",nombre.lower())
#replace -> lo que hace es reemplazar una letra por otra de acuerdo a la letra que le digamos, por ejemplo así:
print("nombre.replace('j','l')")
print("aquí nos dimos cuenta que a la j la cambió o reemplazó por l:",nombre.replace('j','l').lower())
#para acceder a cada letra de un string lo que hacemos por indices o posiciones, ejemplo:
print("del nombre jacobo le indicamos que queremos el indice tres y cuatro, nombre[3] y nombre[4], entonces obtenes la:",nombre[3],"y",nombre[4])
#len -> con este puedo averiguar cuántos caracteres o letras tiene mi cadena
print("con len(nombre) puedo averiguar cuántos caracteres o letras tiene mi cadena:",len(nombre))
caena = "hola amiguitos como estan estoy probando la función len"
print(caena)
print(len(caena))
