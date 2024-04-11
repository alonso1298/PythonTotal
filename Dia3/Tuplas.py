#Las tuplas se almacenan en parentesis o sin ellos, pero es comun con parentesis
mi_tuple = (1, 2, 3, 4)
#Pueden contener diferentes tipos de valores
print(mi_tuple)

print(mi_tuple[0])
print(mi_tuple[-2])
#Podemos acceder a sus indices

#Como las tuplas son inmutables no podemos modificar los valores de las mismas
# mi_tuple[0] = 5
#Esto nos daria un error

print('---------------------')

#Podemos anidar tuplas
mi_tuple2 = (1, 2, (10, 20), 4)
#Esto nos muestra el contenido de la tupla
print(mi_tuple[2])
#Si queremos acceder al contenido especifico de la tupla anidada es pasando el indice de la tupla y agregar otro indice para la tupla contenida
print(mi_tuple2[2][0])

print('---------------------')

#Tambien se puede hacer casting (cambiar su tipo) en las tuplas 
mi_tuple2 = list(mi_tuple2)
print(type(mi_tuple2))
print(mi_tuple2)

print('---------------------')

#Podemos asignar el contenido de una tupla a diferentes variables.
t = (1, 2, 3)
x, y, z = t
print(x, y, z) 
#La unica condicion es que tenga el mismo numero de elementos, si no arrojara un error

print('---------------------')

t2 = (1, 2, 3, 1)
#El metodo count pide un valor para saber cuantas veces aparce este mismo
print(t2.count(1))
#Este imprime en la pantalla 2 ya que aparece 2 veces el 1 en la tupla 

print(t2.index(2))
#En este metodo tenemos que ingresar un valor para saber su indice 