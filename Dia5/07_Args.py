#Para que tenga un numero indefinido de parametros lo hacemos con *args
def suma(*args):
    total = 0

    for i in args:
        total += i
    return total

print(suma(5,8,8,4))

print('\n---------------------\n')

#Tambien se puede representar mas simple 
def suma2(*args):
    
    return sum(args)

print(suma2(6,6,7,88,8))

print('\n---------------------\n')

def suma_cuadrados(*args):
    cuadrados = [i ** 2 for i in args]
    return sum(cuadrados)
    
print(suma_cuadrados(1,2,3))

print('\n---------------------\n')

'''
Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, 
y retorne la suma de sus valores absolutos 
(es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).
'''

def suma_absolutos(*args):
    lista_absolutos = []
    for i in args:
        absoluto = abs(i)
        lista_absolutos.append(absoluto)
    return sum(lista_absolutos)
    
print(suma_absolutos(-1,-1,-1))

print('\n---------------------\n')

'''
Crea una función llamada numeros_persona que reciba, 
como primer argumento, un nombre, y a continuación, 
una cantidad indefinida de números.
'''

def numeros_persona(nombre,*args):
    suma_numeros = sum(args)
    return (f'{nombre}, la suma de tus números es {suma_numeros}')
    
print(numeros_persona('Alonso', 5,8,5,8))