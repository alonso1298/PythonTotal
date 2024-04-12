'''
Los generadores son tipos especiales de funciones que
devuelven un iterador que no almacena su contenido
completo en memoria, sino que "demora" la ejecución de una
expresión hasta que su valor se solicita.
'''
#Si queremos una funcion que nos devuelva el numero 4 en este ejemplo lo haremos de las dos formas
def mi_funcion():
    return 4 

def mi_generador():
    #Para el generador tenemos que usar la palabra clave yield que quiere decir producir
    yield 4
    
print(mi_funcion)

print(mi_generador)