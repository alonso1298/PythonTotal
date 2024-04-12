'''
Los decoradores son patrones de diseño en Python utilizados
para dar nueva funcionalidad a objetos (funciones),
modificando su comportamiento sin alterar su estructura: son
funciones que modifican funciones.
'''
def mayusculas(texto):
    print(texto.upper())
    
def minusculas(texto):
    print(texto.lower())
    
#En python como todos son objetos podemos almacenar una funcion en una variable de la siquiente manera 
mi_funcion = mayusculas
mi_funcion('python')

#Tambien se puede pasar como argumento de otra funcion 
def una_fincion(funcion):
    return funcion

#Estoy llamando desde la funcion una funcion a un argumento que es la funcion mayuscula que pide el argumento texto
una_fincion(mayusculas('probando'))

print('\n---------------------\n')

#En python tambien se pueden definir funciones dentro de otras funciones 
#Vamos a decir que vamos a envolver las funciones
def cambiar_letras(tipo):
    
    def mayuscula(texto):
        print(texto.upper())
    
    def minuscula(texto):
        print(texto.lower())
        
    if tipo == 'may':
        return mayuscula
    
    elif tipo == 'min':
        return minuscula

#Cuando llamemos la funcion le vamos a decir que si queremos may o min    
operacion = cambiar_letras('may')

#Ya seleccionada la funcion entonces le pasamos la palabra 
operacion('Palabra')

print('\n---------------------\n')

#Esta funcion va a decorar cualquier funcion que le pasemos y la va a envolver en esos saludos antes y despues

#Se crea una funcion donde reciba otra funcion
def decorar_saludo(funcion):
    
    #Dentro creamos otra funcion que va a recibir la palabra de las funciones mayuscula y minuscula
    def otra_funcion(palabra):
        #Agregamos el 'hola'
        print('Hola')
        #Se va a pasar la funcion ya sea mayuscula o minuscula y recibe la palabra
        funcion(palabra)
        #Se agrega el 'Adios'
        print('Adios')
    #Retorna el resultado de la otra_funcion
    return otra_funcion

#Una forma es como la siguiente
#En una variable almacenamos la funcion que va a decorar y le pasamos la funcion que transforma a mayusculas o minusculas
decorar = decorar_saludo(mayusculas)
#Seguido le pasamos el parametro de la palabra
decorar('Bad Bunny')

print('\n---------------------\n')

#Tambien hay otra forma es que antes de la definicion se pone el decorador 
#Esto le dice a python que antes de que se vaya a ejecutar la funcion esta se envuelva dentro de decorar saludo
@decorar_saludo
def mayuscula(texto):
    print(texto.upper())
 
@decorar_saludo   
def minuscula(texto):
    print(texto.lower())

mayuscula('Raw Alejandro')

minuscula('Mora')

print('\n---------------------\n')

#Si guardo en una variable la funcion decorar_saludo
mayuscula_decorada = decorar_saludo(mayusculas)

#Si yo lo quiero sin saludo simplemente mando a llamar la funcion 
mayusculas('Alonso')

print(' ')

#Pero si lo quoiero con el saludo, mando a llamar la variable mayuscula_decorada
mayuscula_decorada('Alonso')

print(' ')

minuscula_decorada = decorar_saludo(minusculas)

minuscula_decorada('Alonso')