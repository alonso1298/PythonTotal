'''
El modulo pathlib es un componente importante que nos permite maipular rutas de sistemas de archivos de forma rapida 
en cualquier sistema operativo 
'''

from pathlib import Path, PureWindowsPath

carpeta = Path('C:/python/Dia6/prueba.txt')

print('\n---------------------\n')

# PureWindowsPath permite transformar cualquier tipo de ruta en una ruta de Windows 
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)

print('\n---------------------\n')

'''
- Ahora carpeta tiene metodos distitos ya que es un objeto Path
- Con read text es como el metodo anterior .read() pero ahora este es propio de path 
- Tabien es importante saber que con path no es necesario abrir o cerrar el archivo
'''
print(carpeta.read_text())
print('\n---------------------\n')

#Este metodo nos devuelve el nombre del archivo
print(carpeta.name)
print('\n---------------------\n')

#Este nos devuelve la extencion que tiene el archivo 
print(carpeta.suffix)
print('\n---------------------\n')

#Nos dara el nombre sin la extencion 
print(carpeta.stem)
print('\n---------------------\n')

#Tambien hay un metodo que permite saber si un archivo existe 
if not carpeta.exists():
    print('Este archivo no existe')
else: 
    print('Genial, Existe')