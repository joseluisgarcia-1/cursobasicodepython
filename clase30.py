def run():

    mi_diccionario = {
        'llave1': 10, 
        'llave2': 20,
        'llave3': 30
    }
    print(mi_diccionario)
    print("me imprime el valor que tiene la llave 1:",mi_diccionario['llave1'])
    print("me imprime el valor que tiene la llave 2:",mi_diccionario['llave2'])

    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 105768992,
        'Colombia': 50234871
    }
    print(poblacion_paises)
    for pais in poblacion_paises:
        print(pais)
        print()

    #me imprime las llaves  y valores del diccionario
    for pa, pe in poblacion_paises.items():
        print(pa,"tiene",pe,"millones de habitantes")
        #print("tercer for",pe)
        print()
        
    #me imprime las llaves del diccionario
    for pai in poblacion_paises.keys():
        print("cuarto for",pai)
        print()
        
    #me imprime los valores del diccionario
    for p in poblacion_paises.values():
        print("quinto for",p)
        

if __name__ == '__main__':
    run()