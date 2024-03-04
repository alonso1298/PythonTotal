#Al aplicar el metodo range y le ponemos el valor 5 este comenzara en 0 y termiara en 4
for numero in range(5):
    print(numero)

print('\n')
print('---------------------')
print('\n')

#Si quiero que este empiece en 1 agregamos primero el 1 ya que en los parametros el primero es desde donde empieza y el segundo hasta donde
for i in range(1,5):
    print(i)

print('\n')
print('---------------------')
print('\n')

#Si agregamos un tercer parametro este sera el valor para saltearse numeros
for j in range(20,31,2):
    print(j)

print('\n')
print('---------------------')
print('\n')

#Si queremos crear una lista del 1 al 100 lo hacemos con un casting
lista = list(range(1,101))
print(lista)

print('\n')
print('---------------------')
print('\n')

#Para sumar los cuadrados de una lista 
suma_cuadrados = 0 #Inicializamos la variable en 0

for i in range(1,16): #Creamos un ciclo for donde le pasamos una lista del 1 al 15
    suma_cuadrados += i**2 #Por cada ciclo sumamos el valor de la variable mas el cuadrado de cada elemnto

print(f'La suma de los cuadrados es {suma_cuadrados}') #Imprimimos el resultado 