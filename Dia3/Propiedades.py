nombre = 'Alonso'
#print(nombre)
#nombre[4] = "z"
#Esto nos arrojara un error ya que a los str no soportan asignacion

nombre = 'Alonso'
nombre = "Alonzo"
print(nombre)
#lo mejor es reescribir la variable 

n1 = 'Alon'
n2 = 'so'
print(n1 + n2)
#Se pueden concatenar 

n1 = 'Alonso'
print(n1 * 10)
#Tmbien los strings se pueden multiplicar

poema = """Mil pequeños peces blancos 
comosi hirviera
el color del agua"""
print(poema)
#Podemos hacer saltos de línea con """ comillas 
print('agua' in poema)
#También podemos consultar si en un str existe una determinada palabra o caracter
print('sol' not in poema)
#También podemos consultar si una palabra o caracter aparece en el str

print(len(poema))
#Podemos consultar el numero de caracteres de nuestro str