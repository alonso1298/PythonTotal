'''
Puedes encontrarlos con el nombre de métodos mágicos o dunder
methods (del inglés: dunder = double underscore, o doble guión
bajo). Pueden ayudarnos a sobrescribir métodos incorporados de
Python sobre nuestras clases para controlar el resultado devuelto
'''

mi_lista = [1,1,1,1,1,1,1]
print(len(mi_lista))

#Que pasa si yo quiero aplicar el metodo len a una clase creada por mi mismo 
class Objeto():
    pass

mi_objeto = Objeto()
#Aqui recibiremos un error ya que el objeto no tiene largo 
#print(len(mi_objeto))

print('\n---------------------\n')

#Aqui es donde los metodos especiales nos pueden servir 
class CD:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
    
    #Podemos usar el metodo especial __str__
    #Con esto modificamos la forma en la que se comporta el metodo especial str cada vez que lo llame un metodo y ahora muestre lo que queramos que se construya ahi 
    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'
    
    #Podemos definir como se va a comportar el metodo len cuando alguien pida el largo de mi_cd
    def __len__(self):
        #Esto va a retornar el numero de canciones 
        return self.canciones
    
    #Aqui establecemos que cada que eliminemos la instancia esta imprima que se elimino 
    def __del__(self):
        print('Se a eliminado el cd')

mi_cd = CD('Bad Bunny', 'YHLQMDLG', 20)

#Ahora si queremos imprimir mi_cd se puede hacer 
print(mi_cd)

#Ahora tambien podemos impirmir el largo y este nos arojara en numero de canciones que son 20 
print(len(mi_cd))

print('\n---------------------\n')

#La funcion del puedo establecer que quiero eliminar alguna instancia que eh creado 
del mi_cd

#Este print dara un error ya que la instancia se a eliminado 
#print(mi_cd)

print('\n---------------------\n')

'''
Dada la clase Libro, implementa el método especial __str__ para que cada vez que se imprima el objeto, 
devuelva '"{titulo}", de {autor}' (atención: el título debe estar encerrado entre comillas dobles).
'''

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'
    
mi_libro = Libro('El Psicoanalista', 'John Katzenbach', 521)

print(mi_libro)

print('\n---------------------\n')

'''
Dada la clase Libro, implementa el método especial __len__ para que cada vez que se ejecute la función len() sobre el mismo, 
devuelva el número de páginas como número entero.
'''

class Libro2():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas
    
mi_libro2 = Libro2('Jaque al Psicoanalista', 'John Katzenbach', 452)

print(len(mi_libro2))