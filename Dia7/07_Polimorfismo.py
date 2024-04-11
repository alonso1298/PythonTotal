'''
El polimorfismo es el pilar de la POO mediante el cual un mismo
método puede comportarse de diferentes maneras según el
objeto sobre el cual esté actuando, en función de cómo dicho
método ha sido creado para la clase en particular.
'''

class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' Dice muuuuuu')

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' Dice beeeeee')

#Creamos una instancia u objeto de cada una de las clases
vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

#Los 2 animales son capaces de hablar 
vaca1.hablar()
oveja1.hablar()
#Con esto se puede dar a entender que dos objetos distintos pueden ejecutar el metodo con el mismo nombre aunque hagan cosas distintas

print('\n---------------------\n')

#Esta lista tiene 2 objetos de diferentes tipos
animales = [vaca1, oveja1]

#Podemos iterar sobre sus metodos ya que se llaman de la misma manera 
for animal in animales:
    animal.hablar()

print('\n---------------------\n')

#Tambien podemos usar funciones 
def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)

animal_habla(oveja1)