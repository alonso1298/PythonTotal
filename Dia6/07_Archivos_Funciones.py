''' 
Ahora aplicaremos todo lo visto anteriormente para agregarlos a metodos o funciones 
como una funcion para abrir un archivo o para eliminarlo
'''

'''
Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, 
y devuelva su contenido (read).
'''

def abrir_leer(archivo):
    mi_archivo = open(archivo)
    return mi_archivo.read()

'''
Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, 
y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"
'''

def sobrescribir(archivo):
    mi_archivo = open(archivo, 'w')
    mi_archivo.write("contenido eliminado")
    mi_archivo.close()
    mi_archivo = open(archivo, 'r')
    return mi_archivo.read()

'''
Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, 
y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". 
Finalmente, debe cerrar el archivo abierto.
'''

def registro_error(archivo):
    mi_archivo = open(archivo, 'a')
    mi_archivo.write("se ha registrado un error de ejecución")
    mi_archivo.close()
    mi_archivo = open(archivo, 'r')
    return(mi_archivo.read())