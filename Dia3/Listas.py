mi_lista = ['a', 'b', 'c',]
#Podemos saber el numero de elementos de la lista
resultado = len(mi_lista)
print(resultado)

print('---------------------')

#Podemos extraer el valor de uno de esos elementos 
indice = mi_lista[0:1]
print(indice)

print('---------------------')

#Tambien se pueden concatenar las listas
mi_lista2 = ['d', 'e', 'f']
print(mi_lista + mi_lista2)

print('---------------------')

#Si quiero usar las 2 listas juntas se puede hacer una tercera concatenando las otras
mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)

print('---------------------')

#En las listas si se pueden alterar los elementos
mi_lista3[0] = 'alfa'
#Con esto le decimos en el indice 0 ponga la palabra 'Alfa'
print(mi_lista3)

print('---------------------')

#Hay muchos elementos que tienen la listas, presionando un . 
mi_lista3.append('g')
#Este metodo agrega un elemento a la lista
mi_lista3.pop(0)
#Este metodo elmiina un elemento de la lista, si no se le pasa un indice, elimina el ultimo elemento de la lista
eliminado = mi_lista3.pop(0)
# Podemos guardar en una variable el elemento eliminado 
print(mi_lista3)
print(eliminado)

print('---------------------')

lista = ['g', 'o', 'b', 'm', 'c' ]
lista.sort()
# Este metodo ordena una lista
print(lista)
lista.reverse()
#Este metodo ordenas de forma contraria 