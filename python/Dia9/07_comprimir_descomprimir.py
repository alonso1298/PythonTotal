'''
El formato zip permite comprimir archivos sin pérdida de
información, ahorrando espacio de almacenamiento y
manteniendo documentos relacionados en un mismo archivo
.zip.
'''
import zipfile

# #El objeto Zipfile nos pide dos parametros que es el nombre del archivo y el modo de apertura que es w
# mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

# #Al la variable le vamos a escribir el nombre de los archivoa que vamos a guardar
# mi_zip.write('mi_texto_A.txt')
# mi_zip.write('mi_texto_B.txt')

# #Se cierra el archivo
# mi_zip.close()

print('\n---------------------\n')

#Para descomprimir los archivos es de la siguiente manera

zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')

#Con extractall se extraen todos los archivos 
zip_abierto.extractall()

print('\n---------------------\n')

import shutil

# carpeta_origen = 'C:\\Users\\yo_al\\Documentos\\MisDocumentos'

# archivo_destino = 'Todo_comprimido'

# shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

#Para descomprimir es de la siguiente manetra
shutil.unpack_archive('Todo_comprimido.zip', 'Extraccion terminada', 'zip')