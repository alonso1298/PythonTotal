'''
El módulo Shutil ofrece funcionalidades de alto nivel sobre
archivos, tales como copiar, crear, eliminar y mover entre
directorios. También mencionaremos métodos del módulo os
que cumplen objetivos similares.
'''

import os 
import shutil
import send2trash

#Con getcwd vemos el directorio actual donde me encuentro
print(os.getcwd)

#Abro un nurvo archivo llamado 'curso.txt' pero como no existe lo va a crear
#archivo = open('curso.txt', 'w' )
#Escribimos dentro del archivo
#archivo.write('Texto de prueba')
#Cerramos el archivo
#archivo.close()

#Vemos todos los archivos que tenemos en la ruta
print(os.listdir())

#Con move podemos mover los archivos a la ruta que deseamos, primero el nombre del archivo seguido de la ruta destino
#shutil.move('curso.txt', "c:\\Users\\yo_al\\Documentos\\PythonTotal\\python\\Dia9")

#Este metodo elimina todos los archivos de una ruta que se le pase, pero no se recomienda usarlo ya que es muy agresivo 
#shutil.rmtree()

#Mejor usaremos el modulo send2trash que instalamos previamente
#Este se va a la papelera de reciclaje con la posibilidad de volver a restaurarlo
#send2trash.send2trash('curso.txt')


#Walk recorre todos los directorios, carpetas, subcarpetas y archivos que encuentre en su camino dada una ruta
ruta = 'C:\\Users\\yo_al\\Documentos\\MisDocumentos'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')
    print(f'Las sub carpetas son: ')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son: ')
    for arch in archivo:
        #if arch.starwitch('2015'): podemos indicar que solo los que comiencen con ese nimbre nos lo muestre
        print(f'\t{arch}')
    print('\n')
    