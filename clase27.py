import random

def run():
    numero_aleatorio = random.randint(1, 101)
    numero_elegido = int(input("Ingresa un número:" ))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un número más grande")
        else:
            print("Busca un número más pequeño")
        numero_elegido = int(input("Elige un número nuevo: "))
    print("¡Ganaste!")

if __name__ == '__main__':
    run()