"""
Conversor de pesos polombianos a dolares americanos
"""
pesos = float(input("Ingresa el valor de pesos polombianos que quieres convertir a dolares americanos: "))
precio_dolar = 3896
dolares_convertidos = round(pesos/precio_dolar, 2)
print('Tienes $',dolares_convertidos, 'dolares americanos')
"""
como la operación me estaba arrojando demasiados decimales, lo que hice fue colocar el método round despues del valor
y seguido de la coma, el número 2 para decirle que me redondee ese número únicamente con dos decimales
así: round(pesos/precio_dolar, 2)
"""
"""
Conversor de dolares a pesos colombianos
"""
dolares = float(input("Ingresa el valor de dolares americanos que quieres convertir a pesos polombianos: "))
precio_dolar = 3896
pesos_convertidos = round(dolares*precio_dolar, 2)
print('Tienes $',pesos_convertidos, 'pesos polombianos')