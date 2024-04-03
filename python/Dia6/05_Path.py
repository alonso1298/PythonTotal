'''
Cuando creamos una instancia de la clase Path lo hacemos para representar una ruta a un archivo o a un directorio.
- Path es muy util para crear o mover archivos
- Enumerar los archivos que coincidan con una extension o un patron determinado
- Crear rutas de archivos apripiadas para el sistema operativo basadas en colecciones de string
- Path tambien puede transformar cualquier secuencia de strings en un formato de ruta de acceso 
'''

from pathlib import Path

#Le pasamos una lista con dos string y Path la convierte en una ruta de acceso 
guia = Path('Barcelona', 'Sagrada_Familia')
print(guia)