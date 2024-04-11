class Pajaro:

    alas = True 

    def __init__(self, color, especie): 
        self.color = color 
        self.especie = especie

    '''
    Para agregar metodos a la clase se usa la palabra def para que python sepa que vamos a crear una funcion 
    Seguido del nombre del metodo, dentro de las clases siempre tenemos que pasar al menos un argumento que es obligatorio que es la palabra self
    Esta palabra hace referencia a cada instancia o a cada objeto de esa clase 
    '''
    def piar(self):
        print(f'pio, mi color es {self.color}')


    # Si queremos crear un metodo que pida argumentos, se crea el metodo, agregamos self y seguido de los parametros que va a recibir 
    def volar(self, metros):
        #Si invocamos a un atributo necesitamos relacionar a quien pertenece ese atributo 
        print(f'El pajaro ha volado una cantidad de {metros} metros')

piolin = Pajaro('amarillo', 'Cnario')

#Si llamamos el metodo piar este imprimira lo que asignamos en la funcion 
piolin.piar() 
#Ahora si yo llamo el metodo volar, tendre que pasarle el parametro e imprime lo que definimos en la funcion
piolin.volar(50)