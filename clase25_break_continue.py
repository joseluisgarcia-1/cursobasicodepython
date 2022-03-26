"""
en esta función lo que le digo es que me imprima solo los números pares, teniendo en cuenta que al decirle 
contador % 2 != 0, es que el % lo que hace es hacer una división de la cual trae el restante de las divisiones en python
y como todo número dividido entre 2 su restante es 0 entonces identificará eso y lo imprimirá

otra forma de decirlo es que mientras que el comtador se encuentre con un número siendo un número impar no lo va imprimir,
lo salta 
"""
from unicodedata import numeric


def pares():
    for contador in range(7):
        if contador % 2 != 0:
            continue
        print(contador)

def impares():
    for contador in range(7):
        if contador % 2 != 1:
            continue
        print(contador)
"""
lo que le digo en esta función es que me imprima los números del rango desde el 10 al 37, pero si entre esos numeros está el
35, detenga el ciclo
"""

def metodo_break():
    for number in range(10,37):
        print(number)
        if number == 35:
            break

"""
lo que le digo en esta función es que le voy a pasar un texto o palabra y cuando en esa palabra si hay una letra que sea igual a o
detenga el ciclo
"""
def texto():
    text = input("Escribe un texto: ")
    for letra in text:
        #print(letra)
        if letra == 'o':
            break
        print(letra)

if __name__ == '__main__':
    print("***pares y metodo continue***")
    pares()
    print("***impares y metodo continue***")
    impares()
    print("***metodo break***")
    metodo_break()
    texto()