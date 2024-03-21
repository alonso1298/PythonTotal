#Tambien podemos meter condicionales y loops dentro de las funciones
def chequear_3_cifras(numero):#Esta funcion nos dice si un numero es de 3 cifras
    return numero in range(100,1000)#Le decimos que si el numero esta en el rango de 100 a 999
    #Esto nos imprimira o true o false dependiendo del numero 

resultado = chequear_3_cifras(895)
print(resultado)

print('\n---------------------\n')

#Si quiero que cheque todos lo elementos de una lista y nos verifique si es verdad que alguno de esos numero es de 3 cifras
def chequear_tres_cifras(lista):

    for i in lista:#Por cada elemento de la lista
        if i in range(100,1000):#Se verifica si esta en el rango de 3 cifras
            return True #Si lo esta este regresa true
        else:
            pass #Si no lo esta la funcion sigue pasando 
    
    return False #Lo ponemos fuera del loop ya que si lo ponemos al contrario al primer false el loop se corta y no verifica lo demas 

resultado2 = chequear_tres_cifras([55,99,6000])
print(resultado2)

print('\n---------------------\n')

#Si queremos almacenar todos lo numeros que tengan 3 cifras 
def sustraer_3_cifras(lista2):

    lista2_3_cifras = [] #Creamos un varible que contenga una lista vacia 

    for n in lista2:#Por cada elemento en la lista
        if n in range(100,1000): #Si estan en el rango de 3 cifras
            lista2_3_cifras.append(n)#Estas cifras que si esten en el rango se anadiran a la lista
        else:
            pass #Si hay elementos que no cumplen este pasara al siguiente

    return lista2_3_cifras #Retorna el contenido de la lista

resultado3 = sustraer_3_cifras([555,99,600])
print(resultado3)

print('\n---------------------\n')

'''
Crea una función (todos_positivos) que reciba una lista de números como parámetro, 
y devuelva True si todos los valores de una lista son positivos, 
y False si al menos uno de los valores es negativo. 
Crea una lista llamada lista_numeros con valores positivos y negativos.
'''

def todos_positivos(lista_numeros):
    for i in lista_numeros:
        if i < 0: 
            return False
        else:
            pass
    return True
    
resultado4 = todos_positivos([1,3,-5])
print(resultado4)

print('\n---------------------\n')

'''
Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) 
siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.
'''

def suma_menores(lista_numeros2):
    suma = 0
    for i in lista_numeros2:
        if i in range(0,1001):
            suma += i
        else:
            pass
    return suma
        
resultado5 = suma_menores([50, 2000, 51])
print(resultado5)

print('\n---------------------\n')

'''
Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), 
y devuelva el resultado de dicha cuenta.
'''

def cantidad_pares(lista_numeros):
    num = []
    for i in lista_numeros:
        if i % 2 == 0:
            num.append(i)
            cantidad = len(num)
        else:
            pass
    return cantidad
    
resultado6 = cantidad_pares([2,1,2,6])
print(resultado6)