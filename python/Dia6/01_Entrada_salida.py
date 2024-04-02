#Podemos manipular archivos directo desde python 

#Alojamos en una variable la apertura del archivo
mi_archivo =  open('C:\python\Dia6\prueba.txt')

#Como es un elemento de texto tiene una serie de metodos asociados a ese tipo de archivos 
#Con el metodo read se lee el archivo y con print podemos ver el contenido del archivo
#print(mi_archivo.read())

print('\n---------------------\n')

# #El metodo readline nos permite leer solo una linea
# una_liena = mi_archivo.readline()
# print(una_liena)
# #Si sobreescribimos la variable vamos a obtener la segunda y tercera linea
# una_liena = mi_archivo.readline()
# #Si no queremos que se vea el salto de linea podemos aplicar el metodo rstrip
# print(una_liena.rstrip())

# una_liena = mi_archivo.readline()
# #Como estamos trabajando con Strings podemos utilizar todos sus metodos de estos 
# print(una_liena.upper())

print('\n---------------------\n')

# #Tambien podemos iterar en las lienas del archivo
# for i in mi_archivo:
#     print('Aqui dice: ' + i)

print('\n---------------------\n')

# #Esto nos imprime una lista de todas las lineas del archivo
# #Nota* restringir este metodo solo a archivos pequenos porque cada que se cargue readlines se carga todo el archivo 
# todas = mi_archivo.readlines()
# #Ahora podemos aplicar todos los metodos de las listas
# todas = todas.pop()
# print(todas)

print('\n---------------------\n')

#Siempre es bueno cerrar los archivos ya que ahorras espacio en memoria entre otras cosas
mi_archivo.close()
