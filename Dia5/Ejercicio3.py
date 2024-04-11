'''
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.

'''

def verificar_repetido(*args):
    lista_numeros = []
    for i in args:
        lista_numeros.append(i)
    for j in range(len(lista_numeros) - 1):
        if lista_numeros[j] == lista_numeros[j + 1]:
            return True
    return False
        
resultado = verificar_repetido(6,0,5,1,0,3,0,1)

print(resultado)

print('\n---------------------\n')

#Otra forma se hacerlo es de la siguiente manera: 

def ceros_vecinos(*args):
    
    contador = 0 

    for i in args:

        if contador + 1 == len(args):
            return False

        elif args[contador] == 0 and args[contador + 1] == 0 :
            return True
        else:
            contador += 1 

    return False

print(ceros_vecinos(0,8,5,0,6,0))