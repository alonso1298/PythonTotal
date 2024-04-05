# Desde la libreria random importamos el metodo randint, si queremos importar todo es con un *
from random import *

aleatorio = randint(1, 50) #Le pasamos lo parametros del rango  
print(aleatorio)

print('\n---------------------\n')

#Este metodo nos da un valor aleatorio decimal, si agregamos una fura del parentesis el numero que ingresemos es el numero de decimales que recibiremos
aleatorio2 = uniform(1,5),1
print(aleatorio2)
print('\n---------------------\n')

#El metodo randonm no recibe nungun parametro y automatimanete elige un numero decimal entre 0 a 1
aleatorio3 = random()
print(aleatorio3)

print('\n---------------------\n')

#El metodo choise permite trabajar cin una seleccion aleatoria dentro de una lista
colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio4 = choice(colores)
print(aleatorio4)

print('\n---------------------\n')

#El mrtodo shuffle perimite mezclar 
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)