# Este modulo nos ofrece todas las herramientas para interactuar con el directorio del ordenador. 
import os

#Creamos una variable que ataves del modulo os y su metodo getcwd() ya que este metodo nos dice la ruta actual en la que estamos
ruta = os.getcwd()
print(ruta)

print('\n---------------------\n')

#Este metodo nos permite cambiar de directorio o establecer una ruta distinta de trabajo 
ruta2 = os.chdir('C:\\Users\\yo_al\\Documentos\\Resumen Python\\Alternativa')
#Ya con la ruta establecida podemos abrir el archivo 
archivo = open('otro_archivo.txt')
print(archivo.read())

print('\n---------------------\n')

# Con makedirs podemos crear directorios y establecer la ruta
#ruta3 = os.makedirs('C:\\Users\\yo_al\\Documentos\\Resumen Python\\Alternativa\\otra')
'''
Una ruta contiene 2 elementos
El nombre de base: que es basicamente toda la ruta para llegar a la carpeta donde se encuentra el archivo
El nombre del archivo: si se acolpleta con el nombre del archivo se va a obtener una ruta completa con todo y el archivo
'''

print('\n---------------------\n')

#Si tenemos una ruta compuesta por 2 elementos tambien podemos utilizar metodos de os para obtener por separado ambos elementos 
ruta4 = 'C:\\python\\Dia6\\prueba1.txt'

# Pedimos el nombre de base de nuestra ruta y nos imprimira el nombre de base de nuestro elemento 'prueba1.txt'
#elemento = os.path.basename(ruta4)

#Si queremos recibirl el primer elemento de la ruta es con dirname o nombre del directorio 'C:\python\Dia6'
#elemento = os.path.dirname(ruta4)

#En caso de que se quiera recibir ambos elementos pero separados en una tupla que contenga ambos elementos por separado es con split '('C:\\python\\Dia6', 'prueba1.txt')'
elemento = os.path.split(ruta4)
print(elemento)

print('\n---------------------\n')

#Tambien podemos eliminar carpetas utilizando el metodo rmdir()
#os.rmdir('C:\\Users\\yo_al\\Documentos\\Resumen Python\\Alternativa\\otra')

print('\n---------------------\n')

#Para abrir un archivo sin el modulo os creamos una variable donde tenga toda la ruta completa donde se aloja el archivo 
otro_archivo = open('C:\\Users\\yo_al\\Documentos\\Resumen Python\\Alternativa\\otro_archivo.txt')
print(otro_archivo.read())