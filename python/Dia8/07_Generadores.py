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
 
#Al imprimir la funcion esta dvuelve el 4    
print(mi_funcion())

#Al imprimir el generador devuelve que a producido un objeto
print(mi_generador())

#Para mostrar el objeto vamos a guardar el generador en una vairable 
g = mi_generador()

#Usamos la palabra clave next que quiere decir siguiente g
print(next(g))

print('\n---------------------\n')

#Si yo necesito una funcion que me devuelva una lista de numeros del 1 al 4 multiplicado por 10 
def generar_lista():
    lista = []
    for i in range(1,5):
        lista.append(i * 10)
    return lista

#Asi se hace con un generador
def generador_lista():
    for i in range(1,5):
        #Producimos el numero multiplicado por 10
        yield i * 10
        
print(generar_lista())
print(generador_lista())

l = generador_lista()

#Nos va generando el numero mientras vamos imprimiendo 
print(next(l))
print(next(l))
print(next(l))

print('\n---------------------\n')

def generador():
    x = 1
    yield x
    
    x += 1
    yield x
    
    x += 1
    yield x
    
i = generador()

print(next(i))
print(next(i))
print('Si tenemos enmedio, el generador no se interrumpe')
print(next(i))

print('\n---------------------\n')

def contador():
    x = 0
    while True:
        yield x
        x += 1

generador2 = contador()

print(next(generador2))
print(next(generador2))

print('\n---------------------\n')

def tabla_site():
    x = 7
    while True:
        yield x
        x += 7

generador3 = tabla_site()

print(next(generador3))

print('\n---------------------\n') 

def vidas():
    x = 3
    while x > 0:
        yield f"Te queda{'n' if x != 1 else ''} {x} vida{'s' if x != 1 else ''}"
        x -= 1
    yield 'Game Over'

perder_vida = vidas()

print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))

    
