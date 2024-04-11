'''
La herencia es el proceso mediante el cual una clase puede
tomar métodos y atributos de una clase superior, evitando
repetición del código cuando varias clases tienen atributos o
métodos en común.
'''
class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este Animal ah nacido')

# Para heredar clases se pone entre parentesis la clase padre de la cual se hara la Herencia 
class Pajaro(Animal):
    pass

#Esta propiedad me va a indicar de quien se esta heredando las clases
print(Pajaro.__bases__)

#Esta propiedad me permite saber a quien hereda sus clases
print(Animal.__subclasses__())

piolin = Pajaro(2,'Amarillo')

#Apesar de que Pajaro no tiene metodos, puedo usar uno ya que lo esta heredando de Animal
piolin.nacer()

print(piolin.color)