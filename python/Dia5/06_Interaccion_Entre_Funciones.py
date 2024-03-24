from random import shuffle, randint, choice
#Las funciones pueden interactuar entre si usando el resultado como parametro de otra funcion diferente

#Lista inicial 
palitos = ['-', ' --', '---', '-----']

# Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista


#Pedir intento 
def probar_suerte():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input('Elige un numero del 1 al 4: ')
    
    return int(intento)

#Comprobar intento 
def chequear_intento(lista,intento):
    if lista[intento - 1] == '-':
        print('A lavar los platos')
    else:
        print('Te has salvado')

    print(f'Te a tocado {lista[intento - 1]}')

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)

print('\n---------------------\n')

#Se crean 2 varibles que cada uno elige un numero del 1 al 6 
def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return dado1, dado2
    
# Esta funcion recibe 2 argumentos y suma el resultado de los 2 dados y verifica las opciones 
def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f'La suma de tus dados es {suma_dados}. Lamentable'
    elif suma_dados < 10:
        return f'La suma de tus dados es {suma_dados}. Tienes buenas chances'
    elif suma_dados >= 10:
        return f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora'
        
dado1, dado2 = lanzar_dados() #Almacenamos en 2 variables los 2 resultados
resultado = evaluar_jugada(dado1, dado2) #Le pasamos el resultado de la anterior funcion a la nueva funcion
print(resultado) #Imprime el resultado

print('\n---------------------\n')

lista_numeros = [1,2,15,7,2]

def reducir_lista(lista):
    lista_numeros = list(set(lista))
    maximo = max(lista_numeros)
    lista_numeros.remove(maximo)
    return lista_numeros
    
def promedio(lista):
    largo_lista = len(lista)
    suma = 0
    for i in lista:
        suma += i
    resultado = suma / largo_lista
    return resultado
    
lista_reducida = reducir_lista(lista_numeros)
resultado = promedio(lista_reducida)
print(resultado)

print('\n---------------------\n')

lista_numeros = [2,4,6,7,8]

def lanzar_moneda():
    moneda = ['Cara','Cruz']
    resultado = choice(moneda)
    return resultado
    
def probar_suerte(resultado_moneda, lista):
    if resultado_moneda == 'Cara':
        lista.clear()
        print (f'La lista se autodestruirá, {lista}')
        return lista
    else:
        print (f'La lista fue salvada {lista}')
        return lista
        
moneda = lanzar_moneda()
resultado = probar_suerte(moneda, lista_numeros)