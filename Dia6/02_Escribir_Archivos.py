'''
El metodo Open() recibe un parametro mas que es el modo de apertura y solo hay tres modos que se pueden especificar
1: 'r' solo lectura, no es posible hacer modificaciones al archivo, solo lee el contenido y es el que viene por defecto
2: 'W' solo escritura, si el archivo ya existe, este se resetea desde 0 y si no existe, lo crea 
3: 'a' solo escritura al final del archivo, se crea el archivo en caso de que no existiera y en caso de que si existiera, se posiciona el cursor al final, manteniendo el contenido original 
'''

# archivo = open('C:\python\Dia6\prueba.txt', 'r')
# #Si quisieramos escribir en este archivo nos arrojara un error ya que lo tenemos abierto en solo lectura
# archivo.write('Soy el nuevo texto')
# archivo.close()

print('\n---------------------\n')

# #Creamos un nuevo archivo prueba1.txt
# archivo = open('C:\python\Dia6\prueba1.txt', 'w')
# #Este no imprime saltos de linea para arreglar esto se anade el salto de linea \n
# archivo.write('Hola\n')
# archivo.write('mundo')

print('\n---------------------\n')

# archivo = open('C:\python\Dia6\prueba1.txt', 'w')
# # Con el metodo writelines podemos pasarle una lista de Strings 
# #Nota* esto guarda el texto sin espacios ni saltos de linea
# archivo.writelines(['hola', 'mundo', 'aqui', 'estoy'])

print('\n---------------------\n')

archivo = open('C:\python\Dia6\prueba1.txt', 'a')
archivo.write('Bienvenido')

print('\n---------------------\n')

# #Para ver la modificacion del archivo tenemos abrir para modificarlo, luego cerrarlo y abrirlo en modo de lectura para vizualizarlo
# archivo = open("mi_archivo.txt", 'w')
# archivo.write("Nuevo texto")
# archivo.close()
# archivo = open("mi_archivo.txt", 'r')
# print(archivo.read())

print('\n---------------------\n')

archivo.close()