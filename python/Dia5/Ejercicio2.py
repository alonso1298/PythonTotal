'''
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
'''

def ordernar_palabra(palabra):
    lista_caracteres = []
    for i in palabra:
        lista_caracteres.append(i)
    
    # Usamos un conjunto temporal para almacenar los elementos únicos
    conjunto_temporal = set(lista_caracteres)

    # Reconstruimos la lista sin duplicados
    lista_sin_repetidos = list(conjunto_temporal)

    #Ordenamos la lista alfabeticamente con sort()
    lista_sin_repetidos.sort()
    
    return lista_sin_repetidos

resultado = ordernar_palabra('entretenido')
print(resultado)

print('\n---------------------\n')

# Otra forma de hacerlo es la siguiente:

def letras_unicas(palabra):
    
    mi_set = set()

    for letra in palabra:
        mi_set.add(letra)

    mi_lista = list(mi_set)
    mi_lista.sort()

    return mi_lista