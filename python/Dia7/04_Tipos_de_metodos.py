'''
Decoradores: Esto nos va a permitir crear diferentes metodos. 
Metodos de instancia: que son los que hemos estado realizando anteriormente

Metodos de clase: se crean usando el decorados @classmethod

    @classmethod
    def mi_metodo(cls):
        print('algo')
Estos metodos no estan asociados a las instancias de nuestra clase si no a la clase en si misma

Metodos estaticos: Se crea usando @staticmethod
    @staticmethod
    def mi_metodo():
        print('algo')
Estos no aceptan como parametro ni self ni cls, por esto no pueden modificar el estado de la clase ni de la intancia, 
pero pueden aceptar parametros de entrada 
'''

class Pajaro:

    alas = True 

    def __init__(self, color, especie): 
        self.color = color 
        self.especie = especie

    def piar(self):
        print(f'pio, mi color es {self.color}')

    def volar(self, metros):
        print(f'El pajaro ha volado una cantidad de {metros} metros')
        #Metodos de instancia: Pueden acceder a otros metodos: Se accede al metodo piar para que cuando se ejecute volar, se mande llamar a piar
        self.piar()

    #Metodos de instancia: Acceden y modifican atributos del objeto: Este metodo se va a encargar de pintar a cualquier pajaro de negro 
    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        #Metodos de clase: No pueden acceder a los atributos de instancia como seria 'color' 'especie'
        #print(f'Es de color {sefl.color}')
        #Metodos de clase: Si se puede acceder a los atributos de la clase y hasta modificarlos 
        cls.alas = False
        print(Pajaro.alas)


    @staticmethod
    #Metodos estaticos: No se refieren a la clase o a la instancia, por lo cual no lo pueden modificar
    def mirar():
        print('El pajaro mira')


#Metodos de clase: no requiere el argumento posicional self
Pajaro.poner_huevos(5)

piolin = Pajaro('amarillo', 'Canario')

piolin.piar()
piolin.pintar_negro()
piolin.volar(50)
#Metodos de instancia: Podemos modificar el estado de la clase 
piolin.alas = False
print(piolin.alas)


print('\n---------------------\n')

class Personaje:

    def __init__(self, canridad_flecha):
        self.cantidad_flecha = canridad_flecha

    def lanzar_flecha(self):
        self.cantidad_flecha -= 1
        print(f'Ahora tienes {self.cantidad_flecha} flechas')



arquero = Personaje(10)

arquero.lanzar_flecha()
arquero.lanzar_flecha()
    