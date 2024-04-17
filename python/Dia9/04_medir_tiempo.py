'''
Estudiar el tiempo transcurrido durante la ejecución de un
código nos permite conocerlo mejor y tomar decisiones acerca
de la vía más eficiete para resolver un problema. Tenemos dos
módulos que nos ayudarán: time y timeit.
'''
import time
import timeit

def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista



def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

inicio = time.time()
prueba_for(1000000)
final = time.time()
print(final - inicio)

inicio = time.time()
prueba_while(1000000)
final = time.time()
print(final - inicio)


print('\n---------------------\n')

#Timetit tiene la habilidad de identificar con presision el tiempo de ejecucuion de un bloque de codigo que le pasemoss
declaracion = '''
prueba_for(10)
'''

mi_setup = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''

duracion = timeit.timeit(declaracion, mi_setup, number=10000000)
print(duracion)



declaracion2 = '''
prueba_while(10)
'''

mi_setup2 = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''
duracion2 = timeit.timeit(declaracion2, mi_setup2, number=10000000)
print(duracion2)

