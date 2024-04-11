'''
Los argumentos con palabras clave (keyword arguments,
abreviado kwargs), sirven para identificar el argumento por su
nombre, independientemente de la posición en la que se
pasen a su función. Si no se conoce de antemano su cantidad,
se utiliza el parámetro **kwargs que los agrupa en un
diccionario.
'''

def suma(**kwargs):

    total = 0

    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total

print(suma(x=3, y=5, z=2))

print('\n---------------------\n')

def prueba(num1, num2, *args, **kwargs):

    print(f'El primer valor es {num1}')
    print(f'El primer valor es {num2}')

    for i in args:
        print(f'arg = {i}')

    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')

prueba(15, 50, 100, 400, 300, 600, x='uno', y='dos', z='tres')

print('\n---------------------\n')

#Tambien se pueden usar los asterircos del **kwargs para desempacar tuplas, listas o diccionarios
def prueba2(num1, num2, *args, **kwargs):

    print(f'El primer valor es {num1}')
    print(f'El primer valor es {num2}')

    for i in args:
        print(f'arg = {i}')

    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')

args = [100,200,300,400]
kwargs = {'x':'uno','y':'dos','z':'tres'}

prueba2(15, 50, *args, **kwargs)

print('\n---------------------\n')

'''
Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, 
y devuelva esa cantidad como resultado.
'''

def cantidad_atributos(**kwargs):
    cantidad = 0
    for i in kwargs:
        cantidad += 1
    return cantidad
    
resultado = cantidad_atributos(x=3, y=5, z=2)
print(resultado)

print('\n---------------------\n')

'''
Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). 
La función debe preveer recibir cualquier cantidad de argumentos de este tipo.
'''
def lista_atributos(**kwargs):
    lista_valores = list(kwargs.values())
    return lista_valores
    
resultado = lista_atributos(x='uno', y='dos', z='tres')
print(resultado)

print('\n---------------------\n')

'''
Crea una función llamada describir_persona, que tome como parámetros su nombre y 
luego una cantidad indetermida de argumentos. 
'''
def describir_persona(nombre,**kwargs):
    print(f'Características de {nombre}: ')
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')
        
describir_persona('Alonso', color_ojos = 'cafe', color_pelo = 'castano')