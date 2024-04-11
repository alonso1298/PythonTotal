'''
pathlib proporciona clases para representar rutas de archivos y directorios, 
y ofrece métodos convenientes para manipularlas de manera segura y eficiente.
'''

from pathlib import Path

#Guardamos la ruta del archivo con '/' y al guardarlo con Path permito que cualquier sistema que abra esa ruta lo pueda entender, ya sea con Windows o Mac
carpeta = Path('C:/Users/yo_al/Documentos/Resumen Python/Alternativa')

#Aahora concatenamos el archivo con '/' seguido del nombre del archivo 
archivo = carpeta / 'otro_archivo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())

#De forma alternativa pero menos legible pudimos abrir el archivo en una sola linea de codigo 
# carpeta = Path('C:/Users/yo_al/Documentos/Resumen Python/Alternativa') / 'otro_archivo.txt'