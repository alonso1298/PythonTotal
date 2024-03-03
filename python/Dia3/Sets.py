mi_set = set([1, 2, 3, 4, 5])
print(type(mi_set))
print(mi_set)

#Tmabien se puede declarar un set solo con un juego de llaves 
otro_set = {1, 2, 3, 4, 5}
print(type(otro_set))
print(otro_set)

print('---------------------')

#Los set son elementos unicos y no pueden tener repeticiones
mi_set2 = set([1, 2, 3, 4, 5, 1, 1, 2, 2, 2])
#Al haber elementos repetivos en un set, este los descarta inmediatamente
print(mi_set2)

print('---------------------')

mi_set3 = set([1, 2, 3,(1, 2, 3), 4, 5])
#Los sets solo admiten tuplas, NO admite tuplas ni diccionarios
print(mi_set3)

print('---------------------')

#En los sets podemos utilizar el metodo len 
print(len(mi_set))
#Tambien se pueden hacer consultas
print(2 in mi_set)

print('---------------------')

#Tambien se pueden unir los sets 
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)

#El metodo add nos permite agregar un elemento
s1.add(4)
print(s1)

#El metodo remove peromite eliminar un elemento
s1.remove(2)
print(s1)

#El metodo discar tambien permite remover elementos, la diferencia es que si eleminiamos un elemento que no existe no da error
s1.discard(6)

#El metodo pop si no le pasas un parametro este eleminia un elemento al azar
sorteo = s2.pop()
print(sorteo)