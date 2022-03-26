"""
lo que le decimos es que contador lo iniciamos en 1, y mientras que ese contador sea menor a 1000
a contador que lo iniciamos en 1 súmele 1 entonces luego va valer 2 y así sucesivamente hasta llegar a 
1000 cuando llegue a 1000, detenga el ciclo
"""
# print("ciclo while")
# contador = 1
# print(contador)
# while contador < 1000:
#     contador += 1
#     print(contador)
# print()

print("a = range(100) lo que nos dice es que ese rango de numéros va ir desde el 0 hasta el número antes del 100, es decir el 99:",range(100))
"""
ahora lo que hacemos es colocar ese rango de números dentro de una lista con list, así:
a = list(range(100)) y nos imprime en una lista los números desde el 0 al 99
"""
a = list(range(100))
print(a)
print("ciclo for")
""""ciclo for
lo que le estoy diciendo es para el contador imprimame en el rango de numéros desde 92 hasta el número antes del 100, es decir, el 99
"""
for contador in range(92,100):
    print(contador)

print("con for vamos a imprimir la tabla del 11 de la siguiente manera for i in range(10): print(11*i)")
for i in range(1,11):
    print(11*i)