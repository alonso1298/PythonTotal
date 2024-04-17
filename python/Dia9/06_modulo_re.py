'''
Una expresión regular es una secuencia de caracteres que
forman un patrón de búsqueda determinado. Pueden ser
utilizadas para verificar strings en búsqueda de un contenido
(patrón) específico. Utilizamos el módulo re en Python.
'''

import re

texto = 'Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online'

#Para buscar una palabra lo haciamos de esta manera
palabra = 'ayuda' in texto
print(palabra)

print('\n---------------------\n')

patron = 'ayuda'
busqueda = re.search(patron, texto)
print(busqueda)
#Este nos muestra solo la ubicacion
print(busqueda.span())
#Nos muestra desde donde inicia la palabra 
print(busqueda.start())
#Nos muestra desde donde termina la palabra 
print(busqueda.end())

print('\n---------------------\n')

#Como tenemos 2 palabras 'ayuda' si quiero encontrar mas de una es con find all 
busqueda2 = re.findall(patron, texto)
#Nos arroja una lista con todas las palabra que encontro
print(busqueda2)

print('\n---------------------\n')

#Si queremos saber las ubicaciones de los 2 elementos tenemos que iterar con finiter
for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())


print('\n-----------------------------------\n')


enunciado = 'llama al 564-525-6588 ya mismo'

#Ahora el patron sera una seri de caracteres separados por un guion
patron2 = r'\d{3}-\d{3}-\d{4}'

#A la busqueda le pasamos el patron, seguido del texto donde se va a buscar
resultado = re.search(patron2, enunciado)
print(resultado)
#Si le pasamos el metodo group este nos dara solo el numero encontrado
print(resultado.group())

#Tambien podemos compilarlos 
patron3 = (r'(\d{3})-(\d{3})-(\d{4})')

resultado2 = re.search(patron3, enunciado)
#Nos muestra el segundo elemento del grupo
#NOTA* los indices de busqueda inician desde el uno 
print(resultado2.group(2))

print('\n---------------------\n')

'''
Esto tiene varios usos practicos por ejemplo si un usuario quiere generar una clave 
y queremos controlar que cumpla con algunas condiciones.
Que enpiece con una letra y que en total tenga 8 caracteres
'''

clave = input('Clave: ')

patron = r"\D{1}\w{7}"

chequear = re.search(patron, clave)

print(chequear)

print('\n---------------------\n')

#Tambien tenemos operadores especiales 

info = 'No atendemos los lunes por la tarde'

#Con el caracter | podemos buscar si esta una palabra u otra diferente dentro del texto
#Esto se puede usar para buscar plurales y singulares
buscar = re.search(r'lunes|martes', info)
print(buscar)
#Tambien tenemos comodines como el punto (.) si las ponemos antes o despues este nos traera el texto
buscar2 = re.search(r'....demos.....', info)
print(buscar2)

#Este comodin ^ nos permite verificar el primer caracter, en este caso le estamos preguntando si el primer caracter no es un digito
buscar3 = re.search(r'^\D', info)
print(buscar3)

#Este comodin $ nos permite verificar el ultimo caracter, en este caso le estamos preguntando si el ultimo caracter no es un digito
buscar4 = re.search(r'\D$', info)
print(buscar4)

print('\n---------------------\n')

buscar5 = re.findall(r'[^\s]', info)
print(buscar5)

