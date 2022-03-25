#funciones que imprimen las palabras en el orden inverso
# def alreves():
#     palabra = input("ingresa una palabra: ")
#     inversa = palabra[::-1]
#     print(inversa)
# alreves()

# def alreves_dos(string):
#     inversa = string[::-1]
#     #print(inversa)
#     return inversa
# funcion = alreves_dos("carro")
# print(funcion)
def palindromo(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra_invertida == palabra:
        return True
    else:
        return False
def run():
    palabra = input("Ingrese la palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print(palabra,"es palíndromo")
    else:
        print(palabra,"no es palíndromo")
if __name__ == '__main__':
    run()