lista = ['a', 'b', 'c', 'd']

#Aqui le decimos que por cada letra en lista, imprima cada una
for letra in lista:
#Se puede concatenar 
    print('Letra: ' + letra)

print('--------------------------')

#Podemos obtener el indice
for letra in lista:
#Usamos el metodo index para que nos de el indice y si queremos que empiece por el 1 pues sumamos 1
    numero_letra = lista.index(letra) + 1
    print(f'Letra {numero_letra}: {letra}')

print('--------------------------')

lista2 = ['pablo', 'laura', 'fede', 'luis', 'julia']

#Podemos combinar el for con el if
for nombre in lista2:
#Ahora cada que hace el bucle hace una verificacion si el nombre comienza con la letra l
    if nombre.startswith('l'):
        print(nombre)
#En caso de que no comience con l va a imprimir el nombre que no comienza con la letra
    else:
        print('Nombre que no comienza con L')

print('--------------------------')

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
#Aqui le estamos diciendo al ciclo que a la variable "mi_valor" sea igual a su mismo valor y le sume el numero contenido en la lista numeros 
    mi_valor = mi_valor + numero

#Cuando el loop terime, imprimire el valor de "mi_valor"
print(mi_valor)
#NOTA* Al estar el print al mismo nivel que el for, este se ejecuto al terminar el loop

print('--------------------------')

palabra = 'python'

for letra in palabra:
    print(letra)

#Se pueden iterar listas, str, tuplas, listas que contengan listas
#NOTA* podemos ingresar el String o las listas directamente en el for    
for objeto in [[1,2],[3,4],[5,6]]:
    print(objeto)
#Este imprime los objetos compuestos

print('--------------------------') 

#Si se quiere imprimir cada objeto de esa lista usaremos 2 variables
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)
#Esto pasa porque porque en el primer loop a se carga con la informacion 1 y b con la 2 y asi sucesivamente
    
print('--------------------------') 

#Se oueden iterar diccionarios 
dic = {'clave1':'a', 'clave':'b', 'clave3':'c'}
#Para ver el valor se hace con .items(), si solo queremos los valores es con .values()
for item in dic.items():
    print(item)

#Tambien se puede hacer con dos variables para que se muestre la clave y valor
for a,b in dic.items():
    print(a,b)

print('--------------------------') 

#Para hacer solo la suma de los pares e impares
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
#Se inicializan la variables en 0
suma_pares = 0
suma_impares = 0

for i in lista_numeros:
    if i % 2 == 0: #Verificamos si el numero i es par
        suma_pares = suma_pares + i
        #Si es par la variable "suma_pares" toma su mismo valor y se le suma i
    else:
#Si no lo es entonces la variable "suma_impares" toma su mismo valor y se le suma i
        suma_impares = suma_impares + i
        
print(suma_pares)
print(suma_impares)