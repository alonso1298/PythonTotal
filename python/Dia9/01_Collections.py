'''
El módulo Collections amplía los tipos de contenedores
disponibles en Python. Un contenedor almacena diferentes
objetos y proporciona una nueva forma de acceder e iterar
sobre los mismos.
'''
from collections import Counter, defaultdict, namedtuple, deque

#Supongamos que tenemos una lista de numeros que se van a repetir aleatoriamente
numeros = [6,8,6,5,4,8,6,3,4,8,7,1,2]
#Si yo quiero saber cuantas veces se repite cada uno de los numeros que tiene la lista de numeros, usaremos el objeto counter
print(Counter(numeros))
#Esto nos imprime una especie de diccionario donde tenemos el numero seguido de cuantas veces se repite

#Tambien podemos contar elementos de un string
print(Counter('Misissippi'))

#Tambien se puede contar palabras de una frase
frase = 'al pan pan y al vino vino'
#Usamos el metodo split para separar los elementos por el espacio
print(Counter(frase.split()))

#Tenemos algunos metodos de counter, asignandola a una variable
serie = Counter([1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4])
#Este metodo nos muestra el mas comun al menos comun 
print(serie.most_common())
#Si le pasamos como parametro un uno este nos mostrara el primero que mas se repite
print(serie.most_common(1))
#Si le pasamos como argumento un numero 2 este nos mostrara los 2 numero que mas se repiten
print(serie.most_common(1))
#Si imprimimos una lista creada apartir de los elementos de serie, este nos dara los elementos unicos de la serie
print(list(serie))

print('\n---------------------\n')

mi_dic = {'uno':'verde', 'dos':'azul', 'tres':'rojo'}
print(mi_dic['dos'])
#Si imprimimos una clave que no existe esto nos arrojara un error, y ahi es donde entra defaultdict

#Con esto le estamos diciendo al diccionario que estamos creando que en caso de que no haya una clave, se le asigne el valor 'nada'

otro_dic = defaultdict(lambda: 'nada')

otro_dic['uno'] = 'verde'
#Esto imprimira 'nada'
print(otro_dic['dos'])

#Si imprimimos directamente el diccionario vemos que se a construido un nuevo valor ('dos':'nada') en base a una busqueda que debio arrojar erro
print(otro_dic)

print('\n---------------------\n')

#namedtuple significa como tupla nominada o tupla con nombres
mi_tupla = (500, 68, 10)

print(mi_tupla[1])

#Si tenemos una tupla muy larga donde no recordamos donde encontrar un determinado valor.
#Pero que tal si pudieramos disponer de tuplas a las cuales ademas de acceder a sus valores atraves de su indice, pudieramos acceder atravez de un nomre

#Creamos un objeto persona 
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)

#Si yo quiero acceder a los atributos de ariel puedo hacerlo de la siguiente manera
print(ariel.altura)
print(ariel.peso)

#Tambien se puede acceder a los elementos atravez de su numero de indice 
print(ariel[0])

print('\n---------------------\n')

lista_ciudades = deque(['Londres', 'Berlin', 'Paris', 'Madrid', 'Roma', 'Moscu'])
lista_ciudades.appendleft('CDMX')

print(lista_ciudades)
