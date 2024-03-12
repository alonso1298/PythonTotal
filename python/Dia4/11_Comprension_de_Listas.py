palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

print('\n---------------------\n')

#Para hacer eso mismo con menos lineas de codigo utilizaremos la comprension de listas
palabra2 = 'Python'

# le estamos diciendo que en la variable lista2 sea igual a una lista compuesta de cada elemento va a ser una letra de cada letra que haya en palabra
lista2 = [letra for letra in palabra2] 
print(lista2)

print('\n---------------------\n')

#Tambien se podria hacer en una sola linea poniendo directamente la palabra
lista3 = [i for i in 'PythoN']
print(lista3)

print('\n---------------------\n')

#Tambien se puede trabajar con valores numericos 

lista4 = [n for n in range(0,21,2)]

print(lista4)