class Padre:
    def hablar(self):
        print('hola')

class Madre:
    def reir(self):
        print('ja ja')

    def hablar(self):
        print('que tal')

#Para que la clase hijo herede los metodos de pladre y madre, dentro de los parametros de hijo podemos agregar tantas clases que queremos que hereden
class Hijo(Padre, Madre):
    pass

#Ahora nieto tiene todos lo metodos y atributos de padre y de madre 
class Nieto(Hijo):
    pass


mi_nieto = Nieto()

#Nieto es capaz de hablar ya que todos sus metodos estan heredados de la clase padre 
#NOTA* a pesaque que madre y padre tienen el mismo metodo de hablar, este va a imprimir el del padre ya que esta al princio class Hijo(Padre, Madre)
mi_nieto.hablar()

#Para ver el orden en que va a ir buscando cosas usaremos el metodo especial __mro__ (metod order resolution)
print(Nieto.__mro__)

#Podemos ver que nieto hereda metodos de la madre
mi_nieto.reir()