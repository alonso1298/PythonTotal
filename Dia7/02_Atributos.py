#Existen 2 tipos de atributos, los de clase y los de instancia 

class Pajaro:
    #Para crear un atributo de clase que son iguales para todos los objetos que se van a crear 
    alas = True #Aqui podemos decir que todos los pajaros tienen alas 

    #Para definir los atributos de instancia ya que estos seran diferentes para cada instancia, utilizaremos la palabra def
    #Se asigna el metodo constructor (__init__) que  va asignarles atributos al nuetra clase 
    def __init__(self, color, especie): #Se pasan 2 parametros, el primero es pbligatorio que es la clave "self" que quiere decir 'el mismo'
        self.color = color #self es la instancia del objeto que se va a crear asignandole a su atributo color el parametro color 
        self.especie = especie

#Ahora cuando creamos una instancia de la clase tenemos que pasarle el parametro que creamos 
mi_pajaro = Pajaro('negro', 'Tucan')

#Ahora si llamamos a la instancia que creamos y agregamos un . tenemos el atributo color 
print(mi_pajaro.color) #Al imprimir nos muestra el atributo del pajaro que es 'negro' 
print(mi_pajaro.especie)

#No es necesario crear una instancia para ver el atrinuto de clase ya que todos lo van a tener 
print(Pajaro.alas)
print(mi_pajaro.alas)

print('\n---------------------\n')

class Personaje:
    
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje("Humano", True, 17)

print(harry_potter.real)