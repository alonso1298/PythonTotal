'''
Las clases "hijas" que heredan de las clases superiores, pueden
crear nuevos métodos o sobrescribir los de la clase "padre".
Asimismo, una clase "hija" puede heredar de una o más clases,
y a su vez transmitir herencia a clases "nietas".
'''

class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('En animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')

class Pajaro(Animal):

    #Para crear atributos a una clase heredera tenemos que poner los atributos heredados y el nuevo atributo con el metodo init 
    # def __init__(self, edad, color, altura_vuelo):
    #     self.edad = edad
    #     self.color = color
    #     self.altura_vuelo = altura_vuelo

    #Tambien lo podemos crear con la clase super() y solo se agregan las nuevas
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('Pio')

    def volar(self, metros):
        print(f'El pajaro ah volado {metros} metros')

piolin = Pajaro(3, 'amarillo', 100)
#Si cresmos un nuevo objeto animal, este no nos pedira la altura de vuelo ya que eso solo lo hacen los Pajaros 
mi_animal = Animal(5,'negro')

#Tenemos lo metodos heredados de la clase padre 
piolin.nacer()

#Tambien podemos tener metodos heredados y modificados 
piolin.hablar()

#Tambien puede taner metodos nuevos que no existen en la clase padre
piolin.volar(50)

print('\n---------------------\n')

#Tambien los pajaros podrian tener atributos propios que no se encuentren en los animales como que tan alto vuelan 
print(piolin.altura_vuelo)
