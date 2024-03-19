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

print('\n---------------------\n')

#Podemos hacer operaciones dentro de estas listas 
lista5 = [n / 2 for n in range(0,21,2)]

print(lista5)

print('\n---------------------\n')

#Tambien podemos poner un bloque if para poner los numeros que queramos
lis = [n for n in range(0,21,2) if n * 2 > 10]

print(lis)

print('\n---------------------\n')

#Si queremos ingesar un else entonces este tiene que ir antes del for
lista6 = [n if n * 2 > 10 else 'no' for n in range(0,21,2) ]

print(lista6)

print('\n---------------------\n')

pies = [10,20,30,40,50]
metros = [i / 3.281 for i in pies ]

print(metros)