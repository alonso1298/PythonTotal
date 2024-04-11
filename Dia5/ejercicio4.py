'''
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos.
'''

def contar_primos(num):

    primos = [2]
    iteracion = 3

    if num < 2:
        return 0
    
    while iteracion <= num:

        for n in range(3, iteracion, 2):

            if iteracion % n == 0:
                iteracion += 2
                break
        else: 
            primos.append(iteracion)
            iteracion += 2
    
    print(primos)
    return len(primos)

print(contar_primos(50))