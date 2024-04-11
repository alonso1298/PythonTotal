'''
Cuando creamos una instancia de la clase Path lo hacemos para representar una ruta a un archivo o a un directorio.
- Path es muy util para crear o mover archivos
- Enumerar los archivos que coincidan con una extension o un patron determinado
- Crear rutas de archivos apripiadas para el sistema operativo basadas en colecciones de string
- Path tambien puede transformar cualquier secuencia de strings en un formato de ruta de acceso 
'''

from pathlib import Path

#Podemos utilizar el metodo home dentro de Path para obtener la ruta absoluta a un directorio principal 
base = Path.home()
#Le pasamos una lista con dos string y Path la convierte en una ruta de acceso 
#Al pasarle la base se crea una ruta absoluta
guia = Path(base, 'Barcelona', 'Sagrada_Familia')
print(base)
print(guia)

print('\n---------------------\n')

#El constructor Path acepta tanto cadenas como objetos preexistentes de Path
guia2 = Path(base, 'Europa', 'Espana', Path('Barcelona', 'Sagrada_Familia'))
#Tambien ofrecen una funcion que permite crear de forma sencilla un objeto Path nuevo copiado de otro que ya tenemos pero apuntando a otro objeto distinto 
guia3 = guia2.with_name('La_Pedrera')
print(guia2)
print(guia3)

print('\n---------------------\n')

'''
- Tambien puede resultar util acceder a directorios que estan en medio de la ruta
- parent devuelve el antecesor mas inmediato de una ruta de archivos determinada
 - Miestras mas greguemos el metodo este ira retrocediendo al antecesor 
'''
print(guia2.parent.parent)

print('\n---------------------\n')

#Tambien se puede usar la clase Path para enumerar archivos dentro de un arbol de carpetas
guia4 = Path(Path.home(), 'Europa')

'''
El metodo glob quiere decir global 
Se pone el * ya que indica que son todos
Para que incluya todas las carpetas lo hacemos con **/*
'''
for txt in Path(guia4).glob('**/*.txt'):
    print(txt)

print('\n---------------------\n')

'''
Tambien podemos calcular rutas relacionadas entre si con el metodo relativeto
'''

guia5 = Path('Europa', 'Espana', 'Barcelona', 'Sagrada_Familia.txt')
#Si quiero ver lo que hay en 'Europa' creo una variable que contenga el path guia aplicando el metodo relative to 
en_europa = guia5.relative_to(Path('Europa'))
en_espania = guia5.relative_to(Path('Europa', 'Espana'))
print(en_europa)
print(en_espania)