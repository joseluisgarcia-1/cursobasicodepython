#recorrer una palabra con for
def run():
    plabra = input("ingresa una palabra para recorrer: ")
    for caracter in plabra:
        print(caracter)

def con_mayus():
    palabra_en_mayusculas = input("ingresa una palabra: ")
    for caracter in palabra_en_mayusculas:
        print(caracter.upper())

def con_minus():
    palabra_en_minuscula = input("ingresa una palabra: ")
    for caracter in palabra_en_minuscula:
        print(caracter.lower())

def con_capital():
    palabra_en_capital = input("ingresa una palabra: ")
    for i in palabra_en_capital:
        print(i.capitalize())

if __name__ == '__main__':
    run()
    con_mayus()
    con_minus()
    con_capital()