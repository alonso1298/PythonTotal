#Si necesitamos acceder a los indices de los elementos de una lista lo hacemos con enumerator

#Asi lo haciamos anteriormente.
lista = ['a', 'b', 'c']
indice = 0

for item in lista:
    print(indice, item)
    indice += 1

print('\n---------------------\n')

#Esta es la mejor forma de hacerlo 
for item in enumerate(lista):
    print(item)
#Esto nos imprime una serie de tuplas que contienen cada uno de ellos el indice y luego el objeto

print('\n---------------------\n')

#Si no lo queremos con tuplas lo podemos hacer de la siguiente manera
for i, item in enumerate(lista): #Se crean 2 variables el primero imprime el indice y el segundo el item
    print(i,item)

print('\n---------------------\n')

#Con enumerate tabajar con Strings o Listas, tambien se puede con integers
for j, item in enumerate(range(50, 55)):
    print(j, item)

print('\n---------------------\n')

#Tabien se puede usar fuera de un loop, por ejemplo una lista que se trasforme en una lista de tuplas que contenga en cada tupla al objeto e indice
lista2 = ['a', 'b', 'c']

#Se hace un casting para que entre en una lista y se guarda en una variable
mis_tuples = list(enumerate(lista2))
print(mis_tuples[1][0]) #Para desempacar las tuplas lo hacemos accediendo a su indice con [1] y luego dentro del indice 1 accederemos al indice [0]

print('\n---------------------\n')

#Para añadir una tupla a una lista.
lista_indices = list(enumerate('Python')) #Igualamos la variable a la lista de las tuplas que genera enumerate
print(lista_indices)

print('\n---------------------\n')

#Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres): #Agregamos 2 variables una que contenga el indice y otra el nombre
    if nombre[0] == 'M': #Con una condicion if verificamos en cada uno de los nombres si en su primer indice comienza con M
        print(indice) #Si comienza con M entonces vamos a imprir el indice
    else:
        continue #Si encuentra otro nombre que no comience con M este va a continuarl hasta recorrer toda la lista